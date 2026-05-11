import requests
import json
import redis
from pathlib import Path
from gui import gui

import subprocess
import atexit

subprocess.Popen(["redis-server"])


r = redis.Redis(host = 'localHost', port = 6379 , decode_responses = True)

CONDITION_IMAGE_MAP = {
    "clear":        "clear.png",
    "sunny":        "sunny.png",
    "partly cloudy":"partly_cloudy.png",
    "cloudy":       "cloudy.png",
    "overcast":     "cloudy.png",
    "rain":         "rain.png",
    "drizzle":      "rain.png",
    "snow":         "snow.png",
    "thunder":      "thunder.png",
    "fog":          "fog.png",
}

IMAGES_DIR = Path(__file__).resolve().parent / "source"

def get_image_path(condition: str) -> str | None:
    condition_lower = condition.lower()
    for key, filename in CONDITION_IMAGE_MAP.items():
        if key in condition_lower:
            path = IMAGES_DIR / filename
            return str(path) if path.exists() else None
    return None



def buscar_ciudad(ciudad, update_ui):
    # Intentar desde caché
    cached = r.get(f"weather:{ciudad}")
    if cached:
        import json
        data = json.loads(cached)
        temp, condition = data["temp"], data["condition"]
    else:
        url = (
            "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/"
            + ciudad
            + "?unitGroup=metric&include=current&key=U9MCVCSAG2JTLJBQH9FH8F27Q&contentType=json"
        )
        response = requests.get(url)
        estado = response.json()
        estadoActual = estado["currentConditions"]
        temp = estadoActual["temp"]
        condition = estadoActual["conditions"]

        # Guardar en caché por 10 minutos
        import json
        r.setex(f"weather:{ciudad}", 600, json.dumps({"temp": temp, "condition": condition}))

    image_path = get_image_path(condition)
    update_ui(ciudad, temp, condition, image_path)

gui.create_layout(on_search_callback=buscar_ciudad)
atexit.register(lambda: subprocess.run(["redis-cli", "shutdown", "nosave"]))