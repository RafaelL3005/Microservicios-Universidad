from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_create_curso():
    data = {
        "codigo": "C001",
        "nombre": "Matemática",
        "creditos": 4,
        "docente": "Dr. Lopez"
    }

    response = client.post("/cursos", json=data)
    assert response.status_code == 200