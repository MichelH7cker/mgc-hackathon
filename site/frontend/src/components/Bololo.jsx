
export default function Bololo(info) {

    return (
        <>
        <div className="h-screen bg-gray-300 flex items-center justify-center">
            <div className="bg-gray-200 w-9/12 h-5/6 flex shadow-2xl">
                <div className="w-1/3 flex flex-col gap-20 text-center items-center">
                    <h1 className="font-poppins font-black text-7xl mt-40">Forms</h1>
                    <input type="text" className="bg-blue-500 w-96 h-16 rounded-2xl"/>
                    <input type="text" className="bg-blue-500 w-96 h-16 rounded-2xl"/>
                    <button className="bg-purple-500 w-96 h-16 rounded-2xl text-4xl font-poppins text-white font-black">Entrar</button>
                </div>
                <div className="w-2/3 flex items-center justify-center border-l-2">
                    <img src="./magalu.png" alt="Magalu" className="w-5/6"/>
                </div>
            </div>
        </div>
        </>
    )
}