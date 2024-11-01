from pydantic import BaseModel

class ManifestModel(BaseModel):
    message: str