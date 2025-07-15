import requests
import base64

YOLO_URL = "http://yolo-detector:8000/detect"
GEMINI_URL = "http://gemini-analyzer:8000/analyze"

def process_vehicle_analysis(image_bytes: bytes) -> dict:
    # Paso 1: Enviar imagen original al servicio YOLO
    yolo_response = requests.post(
        YOLO_URL,
        files={"file": ("vehicle.jpg", image_bytes, "image/jpeg")}
    )

    if yolo_response.status_code != 200:
        return {"success": False, "error": "YOLO detection failed", "details": yolo_response.text}

    base64_crop = yolo_response.json().get("image_base64")
    if not base64_crop:
        return {"success": False, "error": "No vehicle detected in image"}

    # Paso 2: Enviar imagen recortada a Gemini
    decoded_image = base64.b64decode(base64_crop)
    gemini_response = requests.post(
        GEMINI_URL,
        files={"file": ("recorte.jpg", decoded_image, "image/jpeg")}
    )

    if gemini_response.status_code != 200:
        return {"success": False, "error": "Gemini analysis failed", "details": gemini_response.text}

    return gemini_response.json()
