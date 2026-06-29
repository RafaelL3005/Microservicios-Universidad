from pydantic import BaseModel, ConfigDict, Field

class CursoCreate(BaseModel):
    codigo: str = Field(min_length=2, max_length=10)
    nombre: str = Field(min_length=3)
    creditos: int = Field(gt=0, lt=10)
    docente: str = Field(min_length=3)


class CursoUpdate(BaseModel):
    nombre: str = Field(min_length=3)
    creditos: int = Field(gt=0, lt=10)
    docente: str = Field(min_length=3)


class CursoResponse(BaseModel):
    id: int
    codigo: str
    nombre: str
    creditos: int
    docente: str

    model_config = ConfigDict(from_attributes=True)