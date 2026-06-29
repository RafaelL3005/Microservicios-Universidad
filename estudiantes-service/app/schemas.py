from pydantic import BaseModel, ConfigDict

# ---------------- CREATE (POST)
class EstudianteCreate(BaseModel):
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str


# ---------------- UPDATE (PUT)
class EstudianteUpdate(BaseModel):
    nombres: str
    apellidos: str
    correo: str
    carrera: str


# ---------------- RESPONSE
class EstudianteResponse(BaseModel):
    id: int
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str

    model_config = ConfigDict(from_attributes=True)