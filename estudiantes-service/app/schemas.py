from pydantic import BaseModel

class Estudiante(BaseModel):
    id: int | None = None
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str

    class Config:
        from_attributes = True