from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import Base, engine, SessionLocal
from app import models
from app.schemas import CursoCreate, CursoUpdate, CursoResponse

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


# CREATE
@app.post("/cursos", response_model=CursoResponse)
def crear(curso: CursoCreate, db: Session = Depends(get_db)):
    nuevo = models.Curso(**curso.model_dump())
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo


# READ ALL
@app.get("/cursos", response_model=list[CursoResponse])
def listar(db: Session = Depends(get_db)):
    return db.query(models.Curso).all()


# READ ONE
@app.get("/cursos/{id}", response_model=CursoResponse)
def obtener(id: int, db: Session = Depends(get_db)):
    curso = db.query(models.Curso).filter(models.Curso.id == id).first()

    if not curso:
        raise HTTPException(status_code=404, detail="No encontrado")

    return curso


# UPDATE
@app.put("/cursos/{id}", response_model=CursoResponse)
def actualizar(id: int, curso: CursoUpdate, db: Session = Depends(get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == id).first()

    if not db_curso:
        raise HTTPException(status_code=404, detail="No encontrado")

    db_curso.nombre = curso.nombre
    db_curso.creditos = curso.creditos
    db_curso.docente = curso.docente

    db.commit()
    db.refresh(db_curso)
    return db_curso


# DELETE
@app.delete("/cursos/{id}")
def eliminar(id: int, db: Session = Depends(get_db)):
    db_curso = db.query(models.Curso).filter(models.Curso.id == id).first()

    if not db_curso:
        raise HTTPException(status_code=404, detail="No encontrado")

    db.delete(db_curso)
    db.commit()

    return {"mensaje": "eliminado"}