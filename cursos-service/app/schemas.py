from pydantic import BaseModel

class Curso(BaseModel):
    id: int
    codigo: str
    nombre: str
    creditos: int
    docente: str