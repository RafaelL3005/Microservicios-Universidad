from fastapi import FastAPI
from schemas import Curso

app = FastAPI()

cursos = []

@app.get("/")
def inicio():
    return {"mensaje": "API cursos funcionando"}

@app.get("/cursos")
def listar():
    return cursos

@app.post("/cursos")
def crear(curso: Curso):
    cursos.append(curso)
    return curso

@app.put("/cursos/{id}")
def actualizar(id: int, nuevo: Curso):
    for i in range(len(cursos)):
        if cursos[i].id == id:
            cursos[i] = nuevo
            return {"mensaje": "actualizado"}
    return {"mensaje": "no encontrado"}

@app.delete("/cursos/{id}")
def eliminar(id: int):
    for i in range(len(cursos)):
        if cursos[i].id == id:
            cursos.pop(i)
            return {"mensaje": "eliminado"}
    return {"mensaje": "no encontrado"}