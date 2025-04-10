"""
Módulo de pruebas para la API de sincronización horaria.

Utiliza pytest y FastAPI TestClient para validar los endpoints expuestos
por la aplicación principal (`main.py`).

:author: Tu Nombre
"""

from fastapi.testclient import TestClient
from main import app
import ntplib
import datetime

# Cliente de pruebas para la app FastAPI
client = TestClient(app)

# Inicialización del cliente NTP y obtención de fecha actual
servidor_ntp = "ntp.shoa.cl"
c = ntplib.NTPClient()
respuesta = c.request(servidor_ntp)
fecha_actual = datetime.datetime.fromtimestamp(respuesta.tx_time)


def test_response_status():
    """
    Verifica que el endpoint raíz ('/') responde con código HTTP 200.

    :return: None
    :rtype: None
    """
    response = client.get("/")
    assert response.status_code == 200
