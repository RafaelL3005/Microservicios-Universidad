from pydantic import BaseModel

class Estudiante(BaseModel):
    id: int
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str