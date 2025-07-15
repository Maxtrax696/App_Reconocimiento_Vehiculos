'''
SERVIDOR FastAPI
    Definicion de un servidor web.
    Exponer el endpoint POST /detectar para recibir imagenes
    Llama a la funcion de deteccion de detection.py
    Devuelve una imagen recortada del vehiculo detectado
'''
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.detection import detect_vehicle
from app.utils import image_bytes_to_pil, image_to_base64

app = FastAPI()

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    try:
        image = image_bytes_to_pil(await file.read())
        cropped = detect_vehicle(image)

        if cropped is None:
            return JSONResponse(status_code=404, content={"error": "No vehicle detected"})

        base64_img = image_to_base64(cropped)
        return {"success": True, "image_base64": base64_img}

    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
