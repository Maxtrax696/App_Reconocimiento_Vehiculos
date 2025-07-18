import requests
import base64
import json
from Modulo_4_Base.app.database import save_vehicle_data  # Importamos la función de base de datos
import re

YOLO_URL = "http://yolo-detector:8000/detect"
GEMINI_URL = "http://gemini-analyzer:8000/analyze"

def process_vehicle_analysis(image_bytes: bytes) -> dict:
    """Procesa la imagen de un vehículo y guarda los datos en la base de datos."""

    # Paso 1: Enviar la imagen original al servicio YOLO para detectar el vehículo
    yolo_response = requests.post(
        YOLO_URL,
        files={"file": ("vehicle.jpg", image_bytes, "image/jpeg")}
    )

    # Verificamos que YOLO haya respondido correctamente
    if yolo_response.status_code != 200:
        return {"success": False, "error": "YOLO detection failed", "details": yolo_response.text}

    base64_crop = yolo_response.json().get("image_base64")
    if not base64_crop:
        return {"success": False, "error": "No vehicle detected in image"}

    # Paso 2: Enviar la imagen recortada a Gemini para obtener detalles del vehículo
    decoded_image = base64.b64decode(base64_crop)
    gemini_response = requests.post(
        GEMINI_URL,
        files={"file": ("recorte.jpg", decoded_image, "image/jpeg")}
    )

    # Verificamos que Gemini haya respondido correctamente
    if gemini_response.status_code != 200:
        return {"success": False, "error": "Gemini analysis failed", "details": gemini_response.text}

    # Paso 3: Obtener los datos del vehículo desde la respuesta de Gemini
    gemini_data = gemini_response.json()
    raw_response = gemini_data.get("raw_response")

    if raw_response:
        try:
            # Convertimos la respuesta `raw_response` (string JSON) a diccionario
            # Extraer solo el bloque JSON usando expresión regular
            match = re.search(r'\{.*\}', raw_response, re.DOTALL)
            if not match:
                return {"success": False, "error": "No se pudo extraer JSON de la respuesta Gemini"}

            vehicle_info = json.loads(match.group())

            # Extraer datos
            marca = vehicle_info.get("marca")
            modelo = vehicle_info.get("modelo")
            precio_raw = vehicle_info.get("precio", "")
            detalles = vehicle_info.get("reseña")

            # Limpiar precio: eliminar símbolos y dejar solo números
            precio_limpio = ''.join(filter(str.isdigit, precio_raw))
            precio = float(precio_limpio) if precio_limpio else 0.0

            # Imprimir para debug
            print(f"Datos a guardar: marca={marca}, modelo={modelo}, precio={precio}, detalles={detalles}")

            # Paso 4: Guardar los datos en la base de datos
            save_vehicle_data(marca, modelo, precio, detalles)

            return {
                "success": True,
                "data": {
                    "marca": marca,
                    "modelo": modelo,
                    "año": vehicle_info.get("año", ""),
                    "precio": f"${precio:,.2f}",
                    "reseña": detalles,
                    "imagen": f"data:image/jpeg;base64,{base64_crop}"
                }
            }

        except json.JSONDecodeError as e:
            print(f"Error al procesar los datos de Gemini: {e}")
            return {"success": False, "error": "Error procesando los datos de Gemini"}
    else:
        return {"success": False, "error": "No raw_response found in Gemini data"}
