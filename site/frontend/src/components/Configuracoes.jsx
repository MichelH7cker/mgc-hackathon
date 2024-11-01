export default function Configuracoes(info) {
    return (
        <>
        <div className="h-screen bg-gray-300 flex items-center justify-center">
            <div className="p-20 bg-gray-200 w-9/12 h-5/6 flex shadow-2xl">
                <div className="w-1/3 flex flex-col text-center items-center justify-center">
                    <h1 className="font-poppins text-mg-purple text-5xl"><b>Configurações</b></h1>
                    <h1 className="font-poppins text-mg-purple text-1xl text-black text-justify my-5">Digite os requisitos desejados para o seu arquivo <em>terraform</em></h1>
                    <div className="w-full flex flex-col gap-10 text-center items-center justify-center">
                        <textarea type="text" className="bg-white w-full h-16 rounded-2xl border-mg-dark-blue p-3"/>
                        <button className="bg-gradient-to-r from-mg-purple to-mg-dark-blue w-full h-16 rounded-2xl text-4xl font-poppins text-white font-black">
                           gerar 
                        </button>
                    </div>
                </div>
                <div className="w-2/3 flex p-5 items-center justify-center border-l-2">
                    <div className="w-full h-full border-4 border-gray-300 rounded-lg shadow-lg p-2 bg-magalu bg-cover "></div>
                </div>
            </div>
        </div>
        </>
    )
}
