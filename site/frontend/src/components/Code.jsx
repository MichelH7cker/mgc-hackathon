import { useState } from 'react';
import SyntaxHighlighter from 'react-syntax-highlighter';
import { atomOneDark } from 'react-syntax-highlighter/dist/esm/styles/hljs';


export default function Code(info) {
    const code = `
resource "mgc_virtual_machine_instances" "nexgen-front" {
  name     = "nexgen-front"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IPa public IPa public IPa public IPa public IPa public IP    
    delete_public_ip    = false
  }

  ssh_key_name = "michel"
}

resource "mgc_virtual_machine_instances" "nexgen-back" {
  name     = "nexgen-back"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "michel"    = "nexgen-back"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "michel"    = "nexgen-back"
  machine_type = {
    name = "BV2-2-40"
  }
  image = {
    name = "cloud-ubuntu-22.04 LTS"
  }
  network = {
    associate_public_ip = true # If true, will create a public IP
    delete_public_ip    = false
  }

  ssh_key_name = "michel"
}

`
    const [copy, setCopy] = useState(false)

    return (
        <div className='h-full bg-gradient-to-r p-4 from-mg-purple to-mg-dark-blue flex justify-center'>
            <div className='w-1/2 h-full m-20 bg-gray-300 rounded-md'>
                <div className='w-full h-full bg-gray-300 rounded-md overflow-hidden'>
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
                    <button className='bg-gradient-to-r from-mg-purple to-mg-dark-blue justify-center items-center w-1/3 h-10 rounded-md font-jetbrains text-white'> baixar </button> 
                </div>
            </div>
        </div>
    )
}
