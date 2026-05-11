import requests
import json
import redis
from gui import gui



r = redis.Redis(host = 'localHost', port = 6379 , decode_responses = True)

def buscar_ciudad(ciudad):
    url = (
        "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
        + ciudad
        + "?unitGroup=metric&include=current&key=U9MCVCSAG2JTLJBQH9FH8F27Q&contentType=json"
    )
    request = requests.get(url)
    estado = request.json()
    estadoActual = estado["currentConditions"]
    print("Temperatura:", estadoActual["temp"])
    print("Condición:", estadoActual["conditions"])

gui.create_layout(on_search_callback=buscar_ciudad)
