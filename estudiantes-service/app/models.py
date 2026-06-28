from sqlalchemy import Column, Integer, String
from database import Base

class Estudiante(Base):
    __tablename__ = "estudiantes"

    id = Column(Integer, primary_key=True, index=True)
    codigo = Column(String(20))
    nombres = Column(String(100))
    apellidos = Column(String(100))
    correo = Column(String(100))
    carrera = Column(String(100))