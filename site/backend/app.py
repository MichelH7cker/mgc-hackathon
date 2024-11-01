from fastapi import FastAPI, HTTPException, Form
from time import time
from log import logger, LoggerMessages
import os
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware
from manifest import Manifest
from models import ManifestModel
from fastapi.responses import FileResponse
from io import BytesIO
import tempfile

# Configurando o middleware CORS
origins = [
    "http://localhost:5173",
    "http://127.0.0.1:3000",
]

# Criar servidor
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Permitir essas origens
    allow_credentials=True,
    allow_methods=["*"],     # Permitir todos os métodos (GET, POST, etc.)
    allow_headers=["*"],     # Permitir todos os cabeçalhos
)

load_dotenv()

# rotas da aplicacao
@app.post("/manifest")
async def get_os(request: ManifestModel) -> dict:
    start_time = time()

    try:
        message = {"message": request.message}

        response = Manifest().generate_tf_code(message=message)

        return {"Response": response}

    except Exception as err:
        logger.error(err)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    finally:
        end_time = time()
        duration = end_time - start_time
        logger.info(LoggerMessages.time_info(duration=duration))

@app.post("/download-manifest")
async def get_os(request: ManifestModel) -> dict:
    start_time = time()

    try:
        message = request.message

        with tempfile.NamedTemporaryFile(delete=False, suffix=".tf") as tmp_file:
            tmp_file.write(message.encode('utf-8'))
            tmp_file_path = tmp_file.name

        return FileResponse(tmp_file_path, media_type="application/octet-stream", filename="main.tf")

    except Exception as err:
        logger.error(err)
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    finally:
        end_time = time()
        duration = end_time - start_time
        logger.info(LoggerMessages.time_info(duration=duration))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host=os.getenv("HOST"), port=int(os.getenv("PORT")))



