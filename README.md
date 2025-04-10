# s1_apps_tecs_web

Una API sencilla desarrollada con **FastAPI** que expone un endpoint para obtener la fecha y hora actual a través de un servidor NTP. Este proyecto está configurado con **Poetry** para la gestión de dependencias y utiliza **uvicorn** como servidor ASGI. Además, incluye pruebas unitarias con **pytest**, un **Dockerfile** optimizado y un flujo de trabajo de **GitHub Actions** para automatizar tareas de linting, testing, construcción y despliegue.

## Índice

- [Características](#características)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso Local](#uso-local)
- [Pruebas](#pruebas)
- [Docker](#docker)
- [Integración Continua](#integración-continua)
- [Documentación del Código](#documentación-del-código)

## Características

- **Gestión de dependencias con Poetry**
- **Endpoints definidos:**  
  - `/` – Mensaje de bienvenida.  
  - `/time` – Consulta NTP y devuelve fecha/hora actual en JSON.
- **Servidor uvicorn** en puerto **8000**.
- **Prueba unitaria** con pytest.
- **Dockerfile** optimizado y funcional.
- **CI/CD con GitHub Actions:** lint, test, build y publish.
- **Código comentado y legible.**

## Requisitos

- Python 3.9
- Poetry
- Docker (opcional)
- Git (opcional)

## Instalación

```bash
git clone https://github.com/tuusuario/s1_apps_tecs_web.git
cd s1_apps_tecs_web
poetry install
```

## Uso Local

```bash
poetry run uvicorn main:app --reload --port 8000
```

- [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
- [http://127.0.0.1:8000/time](http://127.0.0.1:8000/time)

O usando `curl`:

```bash
curl http://127.0.0.1:8000/time
```

## Pruebas

```bash
pytest
```

> Nota: el endpoint `/time` depende del servidor NTP `ntp.shoa.cl`.

## Docker

**Construcción:**

```bash
docker build -t s1_apps_tecs_web .
```

**Ejecución:**

```bash
docker run -p 8000:8000 s1_apps_tecs_web
```

## Integración Continua

El flujo de trabajo (`.github/workflows/main.yml`) realiza automáticamente:

- Lint del código con flake8
- Pruebas con pytest
- Build de imagen Docker
- Push a Docker Hub (configura tus secretos en GitHub)

## Documentación del Código

Revisa:

- `main.py`: aplicación FastAPI
- `test_main.py`: pruebas unitarias
