import requests
import json

request = requests.get("https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Argentina?unitGroup=us&include=current&key=U9MCVCSAG2JTLJBQH9FH8F27Q&contentType=json")



print(json.dumps(request.json(), indent=4, ensure_ascii=False))
