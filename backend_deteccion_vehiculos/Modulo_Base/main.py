from fastapi import FastAPI, Request
from app.database import save_vehicle_data

app = FastAPI()  # ← define app ANTES de usarlo

@app.post("/log")
async def log_data(request: Request):
    data = await request.json()
    try:
        save_vehicle_data(
            data["marca"],
            data["modelo"],
            data["año"],   # o "year" si quieres renombrar todo
            data["precio"],
            data["reseña"]
        )
        return {"success": True}
    except Exception as e:
        return {"success": False, "error": str(e)}
