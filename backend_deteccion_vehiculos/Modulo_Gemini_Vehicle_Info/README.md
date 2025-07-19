# Módulo 2 – Identificación de Vehículos con Gemini 2.0 Flash 🚘✨

Este microservicio utiliza inteligencia artificial generativa para analizar imágenes de vehículos y extraer información relevante como marca, modelo, año, precio estimado y una reseña.

---

## 🧠 ¿Qué hace este servicio?

- Recibe una imagen del usuario por camara o galeria.
- Se conecta con **Gemini 2.0 Flash (Google AI)**.
- Devuelve la información del vehículo en formato JSON.

---

## ⚙️ Tecnologías utilizadas

- FastAPI
- Python 3.10
- Google Generative AI SDK
- Docker

---

## 📁 Estructura

```bash
Modulo_Gemini_Vehicle_Info/
├── app/
│   ├── gemini_client.py    # Establece conexion con API key y version gemini-2.0-flash
│   ├── prompt_builder.py   # Prompt para **analyze_phase**
│   ├── prompt_verifier.py  # Prompt para **verify_phase**
│   ├── analyze_phase.py    # Fase de analisis de imagen ingresada
│   └── verify_phase.py     # Fase de verificacion de imagen ingresada (disponibilidad de vehiculos en la imagen)
├── main.py
├── Dockerfile
├── requirements.txt
├── .env
└── README.md
```

---

## 🚀 Ejecución
  1. Crear archivo .env:
```ini
GEMINI_API_KEY=tu_clave_api
```

  2. Construir y ejecutar:
```bash
  docker build -t gemini-analyzer .
  docker run -p 8001:8000 --env-file .env gemini-analyzer
```

---

## 📤 Endpoint
POST /analyze
  - Entrada: imagen (form-data)
  - Salida: JSON con datos del vehículo

---

## 🧑‍💻 Autores
- Yoshua Calahorrano & John Guerra
- UCE – Minería de Datos – SIS8-001