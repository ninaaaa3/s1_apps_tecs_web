from fastapi import FastAPI
import ntplib
import datetime

servidor_ntp = "ntp.shoa.cl"
c = ntplib.NTPClient()

app = FastAPI()

@app.get("/")
def hello():
    return "/"

@app.get("/time")
def return_datetime():
    respuesta = c.request(servidor_ntp)
    fecha_actual = datetime.datetime.fromtimestamp(respuesta.tx_time)
    return fecha_actual