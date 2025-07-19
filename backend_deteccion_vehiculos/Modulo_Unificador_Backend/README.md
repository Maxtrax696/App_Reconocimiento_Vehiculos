### 📘 Modulo_3_Unificador_Backend

Este microservicio orquesta automáticamente los módulos de detección, análisis y almacenamiento para devolver la información completa del vehículo.

---

## 🔗 ¿Qué hace?

1. Recibe una imagen original desde el frontend o app móvil.
2. Recibe modulo Gemini -> verify_phase para verificar si hay algun vehiculo en la imagen.
3. Reciber modulo Gemini -> analyze_phase para realaizar el analisis de la imagen.
4. Envía los datos al Logger.
5. Retorna la información completa.

---

## ⚙️ Tecnologías utilizadas

- FastAPI
- Python 3.10
- Docker
- Requests

---

## 📁 Estructura

```bash
Modulo_Unificador_Backend/
├── app/
│   └── unifier.py
├── main.py
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## 🔁 Flujo  interno

Usuario
 → /analyze
       → Gemini
         → JSON
           → Logger (MySQL)
             → OK

---

## 🚀 Ejecución

```bash
docker build -t unified-api .
docker run -p 8002:8000 --env-file .env unified-api
```
Acceder a: http://localhost:8002/docs

---

## 📤 Endpoint
POST /analyze
    * Entrada: archivo de imagen (form-data)
    * Salida: JSON con toda la información

---

## 🧑‍💻 Autores
- Yoshua Calahorrano & John Guerra
- UCE – Minería de Datos – SIS8-001