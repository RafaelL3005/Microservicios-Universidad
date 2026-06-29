# Plataforma Web de Gestión Académica


## Descripción

Este proyecto consiste en el desarrollo de una plataforma web basada en arquitectura de microservicios para la gestión de información académica de estudiantes y cursos de la Universidad Tecnológica XYZ.

La solución fue desarrollada utilizando FastAPI y una base de datos SQLite, implementando una API REST para realizar operaciones CRUD sobre estudiantes y cursos.

## Tecnologías utilizadas

* Python 3.13
* FastAPI
* SQLAlchemy
* Pydantic
* SQLite
* Pytest
* Git
* GitHub
* Visual Studio Code

## Estructura del proyecto

### Microservicio de Estudiantes

* Registrar estudiante
* Consultar estudiante
* Listar estudiantes
* Actualizar estudiante
* Eliminar estudiante

### Microservicio de Cursos

* Registrar curso
* Consultar curso
* Listar cursos
* Actualizar curso
* Eliminar curso

## Instalación

1. Clonar el repositorio.

2. Crear el entorno virtual.

```bash
python -m venv venv
```

3. Activar el entorno virtual.

Windows:

```bash
venv\Scripts\activate
```

4. Instalar las dependencias.

```bash
pip install fastapi uvicorn sqlalchemy pydantic email-validator pytest
```

## Ejecución

### Microservicio Estudiantes

```bash
uvicorn app.main:app --reload
```

Acceder a:

```
http://127.0.0.1:8000/docs
```

### Microservicio Cursos

```bash
uvicorn app.main:app --reload
```

Acceder a:

```
http://127.0.0.1:8001/docs
```

## Endpoints

### Estudiantes

| Método | Endpoint          | Descripción           |
| ------ | ----------------- | --------------------- |
| GET    | /                 | Página principal      |
| POST   | /estudiantes      | Registrar estudiante  |
| GET    | /estudiantes      | Listar estudiantes    |
| GET    | /estudiantes/{id} | Consultar estudiante  |
| PUT    | /estudiantes/{id} | Actualizar estudiante |
| DELETE | /estudiantes/{id} | Eliminar estudiante   |

### Cursos

| Método | Endpoint     | Descripción      |
| ------ | ------------ | ---------------- |
| GET    | /            | Página principal |
| POST   | /cursos      | Registrar curso  |
| GET    | /cursos      | Listar cursos    |
| GET    | /cursos/{id} | Consultar curso  |
| PUT    | /cursos/{id} | Actualizar curso |
| DELETE | /cursos/{id} | Eliminar curso   |

## Validaciones implementadas

* Campos obligatorios.
* Validación del formato del correo electrónico.
* Longitud mínima en los campos de texto.
* Validación de créditos como número entero positivo.

## Pruebas

Las pruebas fueron desarrolladas utilizando Pytest.

Ejecutar:

```bash
python -m pytest
```

## Control de versiones

El proyecto fue administrado mediante Git y GitHub para el control de versiones y trabajo colaborativo.

## Autor

Proyecto desarrollado como práctica del curso de Diseño Web.
