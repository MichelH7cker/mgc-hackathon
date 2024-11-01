export default function Bololo(info) {
    return (
        <>
        <div className="h-screen bg-gray-300 flex items-center justify-center">
            <div className="bg-gray-200 w-9/12 h-5/6 flex shadow-2xl">
                <div className="w-1/3 flex flex-col gap-10 text-center items-center justify-center">
                    <h1 className="font-poppins text-mg-purple text-5xl"><b>Configurações</b></h1>
                    <div className="w-1/3 flex flex-col gap-10 text-center items-center justify-center justify-center items-center w-full">
                        <textarea type="text" className="bg-white w-96 h-16 rounded-2xl border-mg-dark-blue p-3"/>
                        <button className="bg-gradient-to-r from-mg-purple to-mg-dark-blue w-96 h-16 rounded-2xl text-4xl font-poppins text-white font-black">Entrar</button>
                    </div>
                </div>
                <div className="w-2/3 flex p-10 items-center justify-center border-l-2">
                    <div className="w-full h-full border-4 border-gray-300 rounded-lg shadow-lg p-2 bg-magalu bg-cover "></div>
                </div>
            </div>
        </div>
        </>
    )
}
