import google.generativeai as genai
import os
import base64

# Leer API Key desde variable de entorno
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def query_gemini(prompt: str, image_base64: str) -> dict:
    model = genai.GenerativeModel("gemini-2.0-flash")
    
    image_bytes = base64.b64decode(image_base64)

    response = model.generate_content(
        [
            prompt,
            {
                "mime_type": "image/jpeg",
                "data": image_bytes
            }
        ]
    )
    
    try:
        return {"success": True, "data": eval(response.text)}  # eval para convertir el JSON string a dict
    except Exception:
        return {"success": False, "raw_response": response.text}
