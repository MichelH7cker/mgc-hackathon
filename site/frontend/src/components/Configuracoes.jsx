import React, { useState } from 'react';
import axios from 'axios';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { atomOneDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';

export default function Configuracoes() {

    const [text, setText] = useState('')
    const [code, setCode] = useState('')
    const [copy, setCopy] = useState(false)
    const [status, setStatus] = useState('idle')

    const handleSubmit = async (e) => {
        e.preventDefault();
        setStatus('loading')
        console.log(text)

        try {
            const response = await axios.post('http://localhost:2000/manifest', {
                message: text,
            });
            
            console.log('Resposta da API:', response);
            setCode(response.data.Response)
            setStatus('idle')

        } catch (error) {
            setStatus('idle')
            console.error('Erro ao enviar o texto:', error);
        }
    }
    
    const handleBaixar = async (e) => {
        e.preventDefault();
        console.log(code)

        try {
            const response = await axios.post('http://localhost:2000/download-manifest', {
                message: code,
            });
            
            const blob = await response.blob();
            const url = window.URL.createObjectURL(blob);

            const link = document.createElement('a');
            link.href = url;
            link.download = 'config.tf';
            link.click();

            window.URL.revokeObjectURL(url);

        } catch (error) {
            console.error('Erro ao enviar o texto:', error);
        }
    }

    return (
        <>
            <form onSubmit={handleSubmit}>
                <div className="h-screen bg-gray-300 flex items-center justify-center">
                    <div className="p-20 bg-gray-200 w-9/12 h-5/6 flex shadow-2xl">
                        <div className="w-1/3 flex flex-col text-center items-center justify-center">
                            <h1 className="font-poppins text-mg-purple text-5xl"><b>Configurações</b></h1>
                            <h1 className="font-poppins text-mg-purple text-1xl text-justify my-5">Digite os requisitos desejados para o seu arquivo <em>terraform</em></h1>
                            <div className="w-full flex flex-col gap-10 text-center items-center justify-center">
                                <textarea type="text" className="bg-white w-full h-16 rounded-2xl border-mg-dark-blue p-3" value={text} onChange={(e) => setText(e.target.value)}/>
                                <button className="bg-gradient-to-r from-mg-purple to-mg-dark-blue w-full h-16 rounded-2xl text-4xl font-poppins text-white font-black">
                                {status == 'idle' ? 'gerar' : 'loading'} 
                                </button>
                            </div>
                        </div>
                        <div className="w-2/3 flex p-5 items-center justify-center border-l-2">
                            <div className="w-full h-full border-4 border-gray-300 rounded-lg shadow-lg p-2 bg-magalu bg-cover "></div>
                        </div>
                    </div>
                </div>
            </form>
            <div className='h-full bg-gradient-to-r p-4 from-mg-purple to-mg-dark-blue flex justify-center'>
                <div className='w-1/2 h-full m-20 bg-gray-300 rounded-md'>
                    <div className='w-full h-full bg-gray-300 rounded-md'>
                        <div className='flex justify-between px-4 text-white text-xs items-center flex-col w-full'>
                            <div className='flex w-full justify-between text-center items-center'>
                                <p className='text-sm text-right text-black'>Terraform code</p>
                                {copy ? (
                                    <button className='py-1 inline-flex items-center gap-1 text-left'>
                                        <span className='text-base mt-1'>
                                            <ion-icon name="checkmark-sharp"></ion-icon>
                                        </span>
                                        Copied!
                                    </button>
                                ) : (
                                    <button className='text-black py-1 inline-flex items-center gap-1' onClick={() => {
                                        navigator.clipboard.writeText(code);
                                        setCopy(true)
                                        setTimeout(() => {
                                            setCopy(false)
                                        }, 3000)
                                    }}>
                                    <span className='text-base mt-1'>
                                        <ion-icon name="clipboard-outline"></ion-icon>
                                    </span>
                                    Copy code
                                </button>
                                )}
                            </div>
                        <SyntaxHighlighter language="terraform" style={atomOneDark} customStyle={{padding: "25px", width: "100%"}}>
                            {code}
                        </SyntaxHighlighter>
                        </div>
                    </div>
                    <div className='w-full m-6 flex justify-center items-center'>
                        <button className='bg-gradient-to-r from-mg-purple to-mg-dark-blue justify-center items-center w-1/3 h-10 rounded-md font-jetbrains text-white' onClick={handleBaixar}> baixar </button> 
                    </div>
                </div>
            </div>
        </>
    )
}
