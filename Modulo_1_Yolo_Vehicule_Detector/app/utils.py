'''
FUNCIONES AUXILIARES
Convertira bytes a imagen (PIL.Image)
Guarda la imagen temporalmente
Validaciones o filtros (pendiente)
'''

from PIL import Image
import io
import base64

def image_bytes_to_pil(image_bytes: bytes) -> Image.Image:
    return Image.open(io.BytesIO(image_bytes)).convert("RGB")

def image_to_base64(image: Image.Image) -> str:
    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")
