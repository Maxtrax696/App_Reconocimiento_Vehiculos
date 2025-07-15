from fastapi import FastAPI, File, UploadFile
from fastapi.responses import JSONResponse
from app.unifier import process_vehicle_analysis

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        result = process_vehicle_analysis(image_bytes)
        return result
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})
