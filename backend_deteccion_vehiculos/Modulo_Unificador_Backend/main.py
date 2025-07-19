from fastapi import FastAPI, UploadFile, File
from app.unifier import analizar_vehiculo

app = FastAPI()

@app.post("/analyze")
async def analyze(file: UploadFile = File(...)):
    result = analizar_vehiculo(file)
    if "error" in result:
        return {"success": False, "error": result["error"]}
    return {"success": True, "data": result}
