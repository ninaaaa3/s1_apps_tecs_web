from fastapi import FastAPI
import ntplib
import datetime

servidor_ntp = "ntp.shoa.cl"
c = ntplib.NTPClient()

app = FastAPI()


@app.get("/")
def hello():
    return "Hello! Go to http://127.0.0.1:8000/time"


@app.get("/time")
def return_datetime():
    try:
        respuesta = c.request(servidor_ntp)
        fecha_actual = datetime.datetime.fromtimestamp(respuesta.tx_time)
        print(fecha_actual)
        return fecha_actual
    except Exception as e:
        print(f'Error de conexión a {servidor_ntp}: {e}')
