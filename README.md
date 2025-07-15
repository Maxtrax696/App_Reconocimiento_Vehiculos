## ## Aplicacion de deteccion de vehiculos con IA Generativa y YOLO

Este proyecto consiste en el desarrollo de un sistema de **identificación de vehículos a partir de imágenes** usando visión por computadora y una aplicacion movil, usando (YOLOv8) e inteligencia artificial generativa (Gemini 2.0 Flash de Google).

---

## 📱 ¿Qué hace el sistema?

1. Un usuario (app móvil) captura la imagen de un vehículo.
2. El backend usa **YOLOv8** para detectar y recortar la región del vehículo.
3. El recorte se envía a **Gemini 2.0 Flash**, que analiza la imagen y genera:
   - Marca del vehículo
   - Modelo
   - Año
   - Precio referencial en Ecuador
   - Breve reseña (respecto a origen del vehiculo y funcionalidad para el consumidor)
4. El sistema responde con toda esta información en formato JSON.

---

## Link de repositorio GitHub
https://github.com/Maxtrax696/App_Reconocimiento_Vehiculos

---

## 🧱 Arquitectura por módulos

```bash
PROYECTO_FINAL/
├── Modulo_1_Yolo_Vehicule_Detector/         # Microservicio de detección (YOLOv8)
├── Modulo_2_Gemini_Vehicle_Info/            # Microservicio de inferencia (Gemini)
├── Modulo_3_Unificador_Backend/             # Microservicio unificado (YOLO + Gemini)
├── docker-compose.yml                       # Orquestador de los 3 servicios
└── docs/                                     # Documentación adicional
```

## ⚙️ Tecnologías utilizadas

| Componente           | Tecnología                   |
| -------------------- | ---------------------------- |
| Backend REST         | Python + FastAPI             |
| Visión computacional | YOLOv8 (`ultralytics`)       |
| IA generativa        | Gemini 2.0 Flash (Google AI) |
| Contenedores         | Docker                       |
| Orquestación         | Docker Compose               |
| Comunicación         | API REST (JSON + Imágenes)   |

---

## 🚀 Cómo levantar Docker Compose

Asegurarse de tener un archivo .env en Modulo_2_Gemini_Vehicle_Info/ con tu API Key ya que en GitHub no se sube el archivo:

```bash
GEMINI_API_KEY=api_key
```
Luego, desde la raíz del proyecto (PROYECTO_FINAL/):

```bash
docker compose up --build
```

Esto levantará automáticamente:
- yolo-detector en http://localhost:8000
- gemini-analyzer en http://localhost:8001
- unified-api en http://localhost:8002

---

## 📦 Flujo de trabajo actual

🔁 Flujo completo con microservicio unificado
1. El usuario sube una imagen a POST /analyze
2. El sistema:
   * Detecta el vehículo con YOLO
   * Recorta automáticamente
   * Analiza la imagen con Gemini
3. Devuelve toda la información del vehículo en formato JSON:

Prueba el endpoint en:
📍 http://localhost:8002/docs

---

## 🧪 Pruebas individuales
También puedes acceder a los microservicios por separado:
   * YOLO → POST /detect en http://localhost:8000
   * Gemini → POST /analyze en http://localhost:8001

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001