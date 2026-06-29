from pydantic import BaseModel, ConfigDict, EmailStr, Field

class EstudianteCreate(BaseModel):
    codigo: str = Field(min_length=2, max_length=10)
    nombres: str = Field(min_length=2)
    apellidos: str = Field(min_length=2)
    correo: EmailStr
    carrera: str = Field(min_length=3)


class EstudianteUpdate(BaseModel):
    nombres: str = Field(min_length=2)
    apellidos: str = Field(min_length=2)
    correo: EmailStr
    carrera: str = Field(min_length=3)


class EstudianteResponse(BaseModel):
    id: int
    codigo: str
    nombres: str
    apellidos: str
    correo: str
    carrera: str

    model_config = ConfigDict(from_attributes=True)