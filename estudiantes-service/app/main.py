from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models
from schemas import Estudiante

app = FastAPI()

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"mensaje": "API Estudiantes funcionando"}

@app.post("/estudiantes")
def crear(estudiante: Estudiante, db: Session = Depends(get_db)):
    nuevo = models.Estudiante(**estudiante.dict(exclude={"id"}))
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/estudiantes")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Estudiante).all()

@app.put("/estudiantes/{id}")
def actualizar(id: int, estudiante: Estudiante, db: Session = Depends(get_db)):
    db_est = db.query(models.Estudiante).filter(models.Estudiante.id == id).first()

    if not db_est:
        return {"mensaje": "no encontrado"}

    db_est.codigo = estudiante.codigo
    db_est.nombres = estudiante.nombres
    db_est.apellidos = estudiante.apellidos
    db_est.correo = estudiante.correo
    db_est.carrera = estudiante.carrera

    db.commit()
    return {"mensaje": "actualizado"}

@app.delete("/estudiantes/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    db_est = db.query(models.Estudiante).filter(models.Estudiante.id == id).first()

    if not db_est:
        return {"mensaje": "no encontrado"}

    db.delete(db_est)
    db.commit()
    return {"mensaje": "eliminado"}