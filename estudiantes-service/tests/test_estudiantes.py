from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"mensaje": "API Estudiantes funcionando"}

def test_create_estudiante():
    data = {
        "codigo": "E001",
        "nombres": "Juan",
        "apellidos": "Perez",
        "correo": "juan@gmail.com",
        "carrera": "Ingeniería"
    }

    response = client.post("/estudiantes", json=data)
    assert response.status_code == 200