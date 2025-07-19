from fastapi import FastAPI, UploadFile, File
from app.verify_phase import verificar_vehiculo
from app.analyze_phase import analizar_vehiculo

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()

        # Fase 1 – Verificación
        veredicto = verificar_vehiculo(image_bytes)
        if isinstance(veredicto, dict) and veredicto.get("success") is False:
            return veredicto

        if veredicto != "un_vehiculo":
            mensajes = {
                "sin_vehiculo": "❌ No se detectó ningún vehículo."
            }
            return {"success": False, "error": mensajes.get(veredicto, f"Respuesta no reconocida: {veredicto}")}

        # Fase 2 – Análisis detallado
        return analizar_vehiculo(image_bytes)

    except Exception as e:
        return {"success": False, "error": str(e)}
