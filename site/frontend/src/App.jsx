import { useState } from "react"
import axios from 'axios'
import { v4 as uuidv4 } from 'uuid';

import "./assets/tailwind.css"

import Configuracoes from './components/Configuracoes'
import Code from './components/Code'

function App() {

    return (
        <>
            <div className="relative flex w-full h-screen bg-gradient-to-r from-fuchsia-500 to-cyan-500">
                <div className='w-1/2 flex flex-col items-start justify-center p-16 gap-20'>
					<div className= "gap-10">
						<h1 className="text-8xl font-bold mb-4 relative z-10 font-poppins text-white "> MagaBot </h1>
						<p className="font-jetbrains text-justify text-2xl text-white mb-6 relative z-10"> 
                            Automatização de Terraform. Utilizamos inteligência artifical para automatizar arquivos de configurações <em>terraform</em> e facilitar o uso da <em>MagaluCloud</em>.
						</p>
					</div> 
                </div>
                <div className='w-1/2 flex items-center justify-center mg-logo'>
                    <div className='w-3/5 h-3/5 items-center justify-center'>
                        <img src='/mg-logo.png' alt='Logo' className='w-full h-full object-contain' />
                     </div>
                </div>
            </div>
            <Configuracoes />
            <Code />
		</>
    )
}

export default App
