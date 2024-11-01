# mgc-hackathon

Este projeto é uma solução completa para a criação de arquivos Terraform de forma automatizada, utilizando uma interface web para capturar inputs dos usuários e um backend que processa as solicitações. Desenvolvido para facilitar a configuração e o provisionamento de infraestrutura na Magalu Cloud, ele permite que o usuário descreva o que deseja, e automaticamente gera os arquivos Terraform necessários usando a API do GPT.

## Funcionalidades

- **Interface Web Intuitiva**: O usuário acessa um site e insere os requisitos de infraestrutura desejados.
- **Processamento em Backend**: O backend captura a solicitação do usuário e aciona um script Python para realizar a chamada à API do GPT.
- **Geração Automática de Terraform**: Com base na descrição fornecida pelo usuário, o backend gera arquivos Terraform customizados, prontos para uso na Magalu Cloud.

## Arquitetura

O projeto é dividido em duas partes principais:

### Frontend

O frontend é a interface web onde os usuários inserem suas requisições. Ele se comunica com o backend para enviar o input do usuário e recebe os arquivos Terraform gerados.

- **Tecnologia**: Desenvolvido em React com o Framework tailwind.

### Backend

O backend é o responsável por processar as requisições dos usuários e acionar a lógica de geração dos arquivos Terraform. 

O site foi hospedado em duas máquinas virtuais na Magalu Cloud. Uma máquina virtual hospedou o frontend do site enquanto que a outra o backend.

- **Tecnologia**: FastAPI. 
- **Integração com a API do GPT**: Utiliza um script Python que chama a API do GPT para interpretar o input e gerar o código Terraform necessário. Inicialmente foi feito um script que convertia toda a documentação do terraform e da magalucloud em um arquivo txt para enviar como entrada para a IA.

## Requisitos de Instalação

**Clonar o Repositório**:
```bash
git clone https://github.com/MichelH7cker/mgc-hackathon
```

## Uso

Entre no site já na nuvem e digite os requisitos e necessidades em cloud. O site gerará um arquivo com as configurações terraform necessárias.

Execute este arquivo com 
```bash
terraform init
```

Planeje sua infraestrutura com
```bash
terraform plan 
```

e finalmente aplique com 
```bash
terraform apply
```
