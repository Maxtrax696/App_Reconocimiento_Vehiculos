from app.gemini_client import gemini_call
from app.prompt_verifier import construir_verificador_prompt

def verificar_vehiculo(image_bytes):
    prompt = construir_verificador_prompt()
    veredicto = gemini_call(prompt, image_bytes)

    if isinstance(veredicto, dict) and veredicto.get("success") is False:
        return {"success": False, "error": veredicto.get("error")}
    
    veredicto = veredicto.strip().lower()
    if veredicto in ["sin_vehiculo", "un_vehiculo"]:
        return veredicto
    return {"success": False, "error": f"Respuesta no reconocida: {veredicto}"}
