# Módulo 3 – Microservicio Unificador 🚀

Este microservicio conecta automáticamente el flujo completo de identificación de vehículos:

1. Recibe una imagen original del vehículo.
2. Llama al microservicio de detección con YOLOv8.
3. Recorta automáticamente la imagen.
4. Llama al microservicio de análisis generativo con Gemini.
5. Devuelve toda la información del vehículo en una única respuesta JSON.
6. El Módulo 4 (Logger API) – para almacenar automáticamente los resultados en una base de datos MySQL.

## 🧱 ESTRUCTURA DEL NUEVO MÓDULO (3)

```bash
Copy code
Modulo_3_Unificador_Backend/
├── app/
│   └── unifier.py          # lógica de conexión entre módulo 1 y 2
├── main.py                 # API REST /analyze
├── requirements.txt        # solo fastapi, requests, python-multipart
├── Dockerfile
├── .env                    # si necesitas claves aquí también
└── README.md
```

## 🔁 Flujo interno

Usuario 
  → /analyze 
    → YOLO (8000) 
      → Imagen Recortada 
        → Gemini (8001) 
          → JSON Analizado 
            → Logger (MySQL vía logger-api) 
              → OK


## ✅ Ejemplo de uso

POST /analyze
Content-Type: multipart/form-data
Body: file=@vehiculo.jpg

### Respuesta (ejemplo):

```json
{
  "success": true,
  "data": {
    "marca": "Kia",
    "modelo": "Sportage",
    "año": "2022",
    "precio": "USD 23,000",
    "reseña": "SUV moderno, eficiente y con buen rendimiento urbano."
  }
}
```

## 🚀 Cómo ejecutar
```bash
docker build -t yolo-integrator .
docker run -p 8002:8000 yolo-integrator
```

Accede a: http://localhost:8002/docs

⚠️ Los microservicios YOLO y Gemini deben estar corriendo en localhost:8000 y localhost:8001 respectivamente.

### Requisitos previos:

Asegúrate de que los siguientes contenedores estén activos:

- `yolo-detector` (Módulo 1)
- `gemini-analyzer` (Módulo 2)
- `logger-api` + `db` (Módulo 4)

Todos deben estar conectados a la red Docker `vehiclenet`.

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001