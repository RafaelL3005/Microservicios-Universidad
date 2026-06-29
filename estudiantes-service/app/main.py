from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app import models
from app.schemas import (
    EstudianteCreate,
    EstudianteUpdate,
    EstudianteResponse
)

app = FastAPI()

# crear tablas
Base.metadata.create_all(bind=engine)

# dependencia DB
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
def home():
    return {"mensaje": "API Estudiantes funcionando"}


# ---------------- CREATE
@app.post("/estudiantes", response_model=EstudianteResponse)
def crear(estudiante: EstudianteCreate, db: Session = Depends(get_db)):
    nuevo = models.Estudiante(**estudiante.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# ---------------- READ ALL
@app.get("/estudiantes", response_model=list[EstudianteResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Estudiante).all()


# ---------------- READ ONE
@app.get("/estudiantes/{id}", response_model=EstudianteResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    est = db.query(models.Estudiante).filter(models.Estudiante.id == id).first()

    if not est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    return est


# ---------------- UPDATE
@app.put("/estudiantes/{id}", response_model=EstudianteResponse)
def actualizar(id: int, estudiante: EstudianteUpdate, db: Session = Depends(get_db)):
    db_est = db.query(models.Estudiante).filter(models.Estudiante.id == id).first()

    if not db_est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    db_est.nombres = estudiante.nombres
    db_est.apellidos = estudiante.apellidos
    db_est.correo = estudiante.correo
    db_est.carrera = estudiante.carrera

    db.commit()
    db.refresh(db_est)
    return db_est


# ---------------- DELETE
@app.delete("/estudiantes/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    db_est = db.query(models.Estudiante).filter(models.Estudiante.id == id).first()

    if not db_est:
        raise HTTPException(status_code=404, detail="Estudiante no encontrado")

    db.delete(db_est)
    db.commit()

    return {"mensaje": "eliminado"}