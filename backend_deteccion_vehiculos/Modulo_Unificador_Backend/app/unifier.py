import requests
import os
import json

GEMINI_URL = os.getenv("GEMINI_URL", "http://gemini-analyzer:8000/analyze")
LOGGER_URL = os.getenv("LOGGER_URL", "http://logger-api:8000/log")

def analizar_vehiculo(imagen):
    try:
        files = {"file": imagen.file}
        response = requests.post(GEMINI_URL, files=files)
        response.raise_for_status()

        resultado = response.json()
        print("📦 Respuesta de Gemini:", resultado)

        if not resultado.get("success", True):
            # Error desde Gemini
            return {"success": False, "error": resultado.get("error", "Error desconocido desde Gemini")}

        # Guardamos en base de datos
        vehicle_data = resultado["data"]
        requests.post(LOGGER_URL, json=vehicle_data)

        return {"success": True, "data": vehicle_data}

    except Exception as e:
        print("❌ Error en unified-api:", e)
        return {"success": False, "error": str(e)}
