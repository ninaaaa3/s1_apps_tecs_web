from fastapi.testclient import TestClient
from main import app
import ntplib
import datetime

client = TestClient(app)

servidor_ntp = "ntp.shoa.cl"
c = ntplib.NTPClient()
respuesta = c.request(servidor_ntp)
fecha_actual = datetime.datetime.fromtimestamp(respuesta.tx_time)


def test_response_status():
    response = client.get("/")
    assert response.status_code == 200
