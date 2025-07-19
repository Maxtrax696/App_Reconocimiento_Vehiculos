import json
import re
from app.gemini_client import gemini_call
from app.prompt_builder import build_prompt

def analizar_vehiculo(image_bytes):
    prompt = build_prompt()
    respuesta = gemini_call(prompt, image_bytes)
    print("📦 Respuesta de Gemini:", respuesta)

    # Intenta parsear directamente como JSON
    try:
        return {"success": True, "data": json.loads(respuesta)}
    except:
        pass

    # Si contiene triple comilla y markdown
    if isinstance(respuesta, str):
        # Limpiar triple backticks, etiquetas json, espacios y saltos
        cleaned = re.sub(r"^```(json)?", "", respuesta.strip(), flags=re.IGNORECASE)
        cleaned = re.sub(r"```$", "", cleaned.strip(), flags=re.IGNORECASE)

        try:
            parsed = json.loads(cleaned)
            return {"success": True, "data": parsed}
        except Exception as err:
            return {
                "success": False,
                "error": f"❌ Error decodificando JSON:\n{cleaned}",
                "raw_response": respuesta
            }

    return {"success": False, "error": "❌ No se pudo procesar la respuesta de Gemini."}
