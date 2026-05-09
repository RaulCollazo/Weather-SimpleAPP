import requests
import json


def requestCiudad ():
    ciudad = str(input("Por favor ingrese su ciudad: "))
    params = {"unitGroup" : "metric" , "key" : "U9MCVCSAG2JTLJBQH9FH8F27Q" , "contentType" : "json" , "include" : "current"}
    url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"+ ciudad +"?unitGroup=metric&include=current&key=U9MCVCSAG2JTLJBQH9FH8F27Q&contentType=json"
    request = requests.get(url , params = params)
    return request

estado = requestCiudad().json()
estadoActual = estado["currentConditions"]

print("Temperatura:", estadoActual["temp"])
print("Condición:", estadoActual["conditions"])

#print(json.dumps(requestCiudad().json(), indent=4, ensure_ascii=False))
