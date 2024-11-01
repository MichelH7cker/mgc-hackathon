import { useState } from "react"
import axios from 'axios'
import { v4 as uuidv4 } from 'uuid';

import "./assets/tailwind.css"

import Stations from './components/Stations'

function App() {

    const [origin, setOrigin] = useState('')
    const [destination, setDestination] = useState('')
    const [option, setOption] = useState() // 'g1', 'g2', 'g3', 'g4'

    const [status, setStatus] = useState('idle') // 'idle', 'loading', 'error', 'ready'
    const [response, setResponse] = useState([])

    const handleClick = () => {
        console.log(origin)
        console.log(destination)
        console.log(option)

        setStatus('loading')
        const searchBaseURL = `http://127.0.0.1:5000/${option}?s1=${origin}&s2=${destination}`
        axios
            .get(searchBaseURL)
            .then((res) => {
                console.log(res, "Response fetched in app")
                setResponse(res.data)
                setStatus('ready')
            })
            .catch((error) => {
                console.log("Erro fetch full criterio: " + error);
                setStatus('error')
            })
    }

    const handleOption = (e) => {
        setOption(e.target.value)
        setStatus('idle')
    }


    return (
        <>
            <div className='flex w-full h-screen bg-gradient-to-r from-mg-purple to-mg-dark-blue'>
                <div className='w-1/2 flex flex-col items-start justify-center p-16 gap-20'>
					<div className= "gap-10">
						<h1 className="text-8xl font-bold mb-4 relative z-10 font-poppins text-white "> Automatização de Terraform </h1>
						<p className="font-jetbrains text-2xl text-white mb-6 relative z-10"> 
                            Utilizamos inteligência artifical para automatizar arquivos de configurações <em>terraform</em> e facilitar o uso da <em>MagaluCloud </em> 
						</p>
					</div> 
                </div>
                <div className='w-1/2 flex items-center justify-center mg-logo'>
                    <div className='w-3/5 h-3/5 items-center justify-center'>
                        <img src='/mg-logo.png' alt='Logo' className='w-full h-full object-contain' />
                     </div>
                </div>
            </div>
		</>
    )
}

export default App
