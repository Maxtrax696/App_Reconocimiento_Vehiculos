from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from app.prompt_builder import build_prompt
from app.gemini_client import query_gemini
from app.utils import image_bytes_to_base64

app = FastAPI()

@app.post("/analyze")
async def analyze_image(file: UploadFile = File(...)):
    try:
        img_bytes = await file.read()
        img_base64 = image_bytes_to_base64(img_bytes)
        prompt = build_prompt()
        result = query_gemini(prompt, img_base64)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
