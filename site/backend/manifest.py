from crewai_tools import TXTSearchTool
from crewai import Agent, Task, Crew, Process
from langchain_openai import ChatOpenAI
import pandas as pd
import os
from example import TF_EXAMPLE
from dotenv import load_dotenv

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

class Manifest:
    def __init__(self, llm_model="gpt-4o", temperature=0, max_retries=2):
        self.tool = TXTSearchTool(txt='documentacao.txt')
        self.model = ChatOpenAI(model=llm_model, temperature=temperature, max_retries=max_retries)

        self.rag_question_agent = self.__create_rag_question_agent()
        self.rag_agent = self.__create_txt_agent()
        self.writer_agent = self.__create_writer_agent()

        self.response = None

    def generate_tf_code(self, message:str) -> str:
        try:
            rag_question_task = self.__create_rag_question_task(agent=self.rag_question_agent, message=message)
            rag_task = self.__create_rag_task(agent=self.rag_agent, message=message, task_context=[rag_question_task])
            writer_task = self.__create_writer_task(agent=self.writer_agent, message=message, task_context=[rag_task])

            crew = self.__create_Crew(agents=[self.rag_question_agent,self.rag_agent,self.writer_agent],
                                    tasks=[rag_question_task,rag_task,writer_task])

            response = crew.kickoff()

            return response.raw.replace("```hcl", "").replace("```", "").strip()

        except Exception as err:
            raise err

    def __create_rag_question_agent(self) -> Agent:
        rag_question_agent = Agent(
            role = "Redator de Prompts",
            goal = "Escrever prompts otimizados voltados para recuperação de inforamção em arquivos PDF.",
            backstory = """
                Você é um redator especialista em IA Generativa, com prática sênior em escrever prompts otimizados e eficientes.
                Sua área de atuação é no setor de infraestrutura de servidores, especialmente com o uso de Terraform.
                Sua especialidade é receber mensagens genéricas e transformá-las em prompts ideais para a tarefa de recuperação de informação. 
            """,
            verbose = False,
            max_iter = 10,
            memory = True,
            allow_delegation = False
        )

        return rag_question_agent

    def __create_txt_agent(self) -> Agent:
        rag_agent = Agent(
            role = "TXT Searcher",
            goal = f"""Faça a recuperação de informações a partir de um arquivo txt.""",
            backstory = """Você é um especialista em recuperação de informação a partir de arquivos textos.
                            Sua experiência é de receber uma mensagem e buscar no arquivo a melhor parte que se relaciona com isso.""",
            verbose = False,
            max_iter = 10,
            memory = True,
            tools = [self.tool],
            allow_delegation = False
        )

        return rag_agent
    
    def __create_writer_agent(self) -> Agent:
        write_agent = Agent(
            role = "Escritor de Arquivos Terraform",
            goal = f"""Escreva um arquivo Terraform de forma atendendo as demandas pedidas.""",
            backstory = f"""
                Você é um planejador sênior com mais de 10 anos de experiência que trabalha na Magalu Cloud, uma grande empresa do setor de cloud brasileiro.  
                Você é especialista em criar arquivos do tipo Terraform para infraestrutura de servidores cloud para atender as demandas de clientes.  
                O texto gerado deve ser voltado para um arquivo Terraform e deve atender todos os pontos pedidos.  
                Opte sempre por usar configurações que visem o equilíbrio entre otimização e escalabilidade.  
                Preze sempre pela segurança.  
                O nome do provedor cloud é **exclusivamente** `mgc_virtual_machine_instances`, e **não** deve ser trocado ou alterado em nenhuma situação.  
                **Não utilize outros nomes para o provedor, como 'magali_cloud', que são incorretos.**
                Segue um exemplo de arquivo Terraform, utilize-o de base, modificando as configurações conforme necessidade do que foi pedido:
                {TF_EXAMPLE}
            """,
            verbose = False,
            max_iter = 10,
            memory = True,
            allow_delegation = False
        )

        return write_agent
    
    def __create_html_transcriptor_agent(self) -> Agent:
        html_transcriptor_agent = Agent(
            role = "Transcrever Markdown em HTML",
            goal = f"""Transcreva um texto Markdown para HTML.""",
            backstory = """
                Você é um especialista em textos markdown e um códigos HTML.
                Sua especialidade é passar um texto em Markdown para um código HTML.
                Gere apenas a seção <body> do código sem incluir a tag <body>.  
            """,
            verbose = False,
            max_iter = 10,
            memory = True,
            allow_delegation = False
        )

        return html_transcriptor_agent

    def __create_rag_question_task(self, agent, message) -> Task:
        rag_question = Task(
            description=f"""
                Com base na mensagem {message}, escreva um prompt otimizado e eficiente para a recuperação de informação em um manual da Magalu Cloud, este manual é um arquivo .txt.
            """,
            agent=agent,
            expected_output="Um prompt eficiente para que o modelo llm possa fazer a recuperação de informação no manual.",
        )

        return rag_question

    def __create_rag_task(self, agent, message, task_context:list[Task]) -> Task:
        rag_task = Task(
            description = f"Com base no prompt gerado pelo 'rag question agent' para a mensagem {message}, faça a recuperação de informação com o arquivo .txt levando em consideração a parte mais relevante para a mensagem recebida.",
            agent = agent,
            expected_output = "A parte do rquivo mais relevante para o prompt.",
            context=task_context
        )

        return rag_task
    
    def __create_writer_task(self, agent, message, task_context:list[Task]) -> Task:
        writer_task = Task(
            description=f"A partir das informações recuperadas pelo 'rag task' para a mensagem {message}, escreva um arquivo Terraform para atender as demandas pedidas.",
            agent=agent,
            expected_output="""
                O conteúdo gerado deve ser um arquivo Terraform completo e funcional.  
                O nome do provedor cloud é **exatamente** `"mgc_virtual_machine"`, e deve ser referenciado como `provider = "mgc_virtual_machine"` no arquivo.  
                **Não utilize qualquer outro nome para o provedor.**  
                Certifique-se de que a configuração contenha todas as informações necessárias para o provisionamento, mantendo o equilíbrio entre otimização, escalabilidade e segurança.
                """,
            context=task_context
        )

        return writer_task
    
    def __create_Crew(self, agents:list[Agent], tasks:list[Task]) -> Crew:
        crew = Crew(
            agents=agents,
            tasks=tasks,
            verbose = False,
            process=Process.hierarchical,
            full_output=True,
            share_crew=False,
            manager_llm=self.model,
            max_iter=10,
        )

        return crew

if __name__ == "__main__":
    message = {"message": "Crie um Terraform para uma máquina virtual de 2 GB de RAM."}

    response = Manifest().execute(message=message)
    print(response)
    print(type(response))