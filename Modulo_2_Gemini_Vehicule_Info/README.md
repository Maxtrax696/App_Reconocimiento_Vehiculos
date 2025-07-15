# Módulo 2 – Identificación de Vehículos con Gemini 2.0 Flash 🚘✨

Este microservicio se encarga de analizar una **imagen recortada de un vehículo** y generar información detallada usando inteligencia artificial generativa.

## 🧠 ¿Qué hace este servicio?

- Recibe una imagen de un vehículo (recortada previamente por YOLO).
- Llama a la API de **Gemini 2.0 Flash** para obtener:
  - Marca
  - Modelo
  - Año aproximado
  - Precio estimado en Ecuador
  - Reseña del vehículo
- Devuelve los datos en formato **JSON**.

## ⚙️ Tecnologías utilizadas

- FastAPI
- Python 3.10
- Google Generative AI SDK (`google-generativeai`)
- Docker

---

## 📦 Estructura del Proyecto

```bash
Modulo_2_Gemini_Vehicle_Info/
  app/
    gemini_client.py    # Lógica de conexión con Gemini
    prompt_builder.py   # Prompt estático
    utils.py            # Conversión base64
  main.py                 # Servidor FastAPI
  requirements.txt        # Dependencias Python
  Dockerfile              # Contenedor
  .env                    # Clave de la API (no subir)
  .gitignore
  README.md
```

---

## 🚀 Cómo ejecutar con Docker

### 1. Asegúrate de tener un archivo `.env` con tu clave:

GEMINI_API_KEY=tu_api_key_de_gemini


### 2. Construir y ejecutar el contenedor

```bash
docker build -t yolo-gemini .
docker run -p 8001:8000 --env-file .env yolo-gemini
```

## 🔍 Cómo usar el endpoint
POST /analyze
Recibe: archivo de imagen (form-data)

Devuelve: JSON con la información del vehículo

## ✍️ Notas
Este servicio debe recibir una imagen recortada, idealmente desde el Módulo 1 (YOLO).

Requiere conexión a internet para acceder a Gemini.

Usa el modelo actualizado gemini-2.0-flash.

## 🧑‍💻 Autores
Universidad Central del Ecuador
Facultad de Ingenieria y Ciencias Aplicadas
Sistemas de Informacion
Mineria de Datos
Yoshua Calahorrano y John Guerra
SIS8-001