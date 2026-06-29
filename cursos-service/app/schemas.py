from pydantic import BaseModel, ConfigDict

class CursoCreate(BaseModel):
    codigo: str
    nombre: str
    creditos: int
    docente: str


class CursoUpdate(BaseModel):
    nombre: str
    creditos: int
    docente: str


class CursoResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    creditos: int
    docente: str

    model_config = ConfigDict(from_attributes=True)