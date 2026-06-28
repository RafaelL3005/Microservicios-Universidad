from pydantic import BaseModel

class Curso(BaseModel):
    id: int | None = None
    codigo: str
    nombre: str
    creditos: int
    docente: str

    class Config:
        from_attributes = True