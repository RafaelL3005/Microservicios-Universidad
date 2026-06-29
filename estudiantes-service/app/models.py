from sqlalchemy import Column, Integer, String
from app.database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String, unique=True, index=True)
    nombres = Column(String)
    apellidos = Column(String)
    correo = Column(String)
    carrera = Column(String)