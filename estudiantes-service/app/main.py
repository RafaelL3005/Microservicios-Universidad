from fastapi import FastAPI
from schemas import Estudiante

app = FastAPI()

estudiantes = []

@app.get("/")
def inicio():
    return {"mensaje": "API funcionando"}

@app.get("/estudiantes")
def listar():
    return estudiantes

@app.post("/estudiantes")
def crear(estudiante: Estudiante):
    estudiantes.append(estudiante)
    return estudiante

@app.put("/estudiantes/{id}")
def actualizar(id: int, nuevo: Estudiante):
    for i in range(len(estudiantes)):
        if estudiantes[i].id == id:
            estudiantes[i] = nuevo
            return {"mensaje": "actualizado"}
    return {"mensaje": "no encontrado"}

@app.delete("/estudiantes/{id}")
def eliminar(id: int):
    for i in range(len(estudiantes)):
        if estudiantes[i].id == id:
            estudiantes.pop(i)
            return {"mensaje": "eliminado"}
    return {"mensaje": "no encontrado"}