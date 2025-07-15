'''
LOGICA DE DETECCION
    Carga el modelo YOLOv8 preentrenado
    Procesa la imagen recibida y detecta el vehiculo
    Recorta la imagen recibida y detecta el vehiculo
    Recorta la region del vehiculo y la devuelve
    Puede rebajar con rutas de archivo o PIL.Image
'''

from ultralytics import YOLO
import numpy as np
from PIL import Image

# Cargar el modelo YOLOv8 (puede ser v8n, v8s, v8m, v8l, v8x)
model = YOLO('yolov8n.pt')  # Cambiar por otro modelo si se desea

def detect_vehicle(image: Image.Image):
    # Convertir imagen PIL a numpy
    frame = np.array(image)

    # Detectar objetos
    results = model(frame)[0]
    detections = results.boxes.data

    if detections.shape[0] == 0:
        return None  # No detecciones

    # Tomamos la primera detección (más probable)
    x1, y1, x2, y2, conf, cls = detections[0].tolist()

    # Recortar región
    x1, y1, x2, y2 = map(int, [x1, y1, x2, y2])
    cropped = image.crop((x1, y1, x2, y2))

    return cropped
