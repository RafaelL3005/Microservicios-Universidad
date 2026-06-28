from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from database import Base, engine, SessionLocal
import models
from schemas import Curso

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
    return {"mensaje": "API Cursos funcionando"}

@app.post("/cursos")
def crear(curso: Curso, db: Session = Depends(get_db)):
    nuevo = models.Curso(**curso.dict(exclude={"id"}))
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

@app.get("/cursos")
def listar(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()

@app.put("/cursos/{id}")
def actualizar(id: int, curso: Curso, db: Session = Depends(get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == id).first()

    if not db_curso:
        return {"mensaje": "no encontrado"}

    db_curso.codigo = curso.codigo
    db_curso.nombre = curso.nombre
    db_curso.creditos = curso.creditos
    db_curso.docente = curso.docente

    db.commit()
    return {"mensaje": "actualizado"}

@app.delete("/cursos/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == id).first()

    if not db_curso:
        return {"mensaje": "no encontrado"}

    db.delete(db_curso)
    db.commit()
    return {"mensaje": "eliminado"}