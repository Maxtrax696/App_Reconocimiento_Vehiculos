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

## 🧱 Arquitectura por módulos

PROYECTO_FINAL/
|    |__ Modulo_1_Yolo_Vehicule_Detector/
|        (detección de vehículos con YOLOv8)
|    |__ Modulo_2_Gemini_Vehicle_Info/
|        (análisis generativo con Google Gemini 2.0 Flash)
|    docs/
|        (documentación complementaria)
|    README.md


---

## ⚙️ Tecnologías utilizadas

| Componente          | Tecnología                     |
|---------------------|--------------------------------|
| Backend REST        | Python + FastAPI               |
| IA visión computacional | YOLOv8 (`ultralytics`)     |
| IA generativa       | Gemini 2.0 Flash (Google AI)   |
| Contenedores        | Docker                         |
| Comunicación        | API HTTP (JSON + imágenes)     |

---

## 🚀 Cómo ejecutar los módulos localmente

### Módulo 1 – Detección con YOLOv8

```bash
cd Modulo_1_Yolo_Vehicule_Detector
docker build -t yolo-detector .
docker run -p 8000:8000 yolo-detector
```
Accede a: http://localhost:8000/docs

## Módulo 2 – Generación con Gemini
```bash
cd Modulo_2_Gemini_Vehicle_Info
docker build -t yolo-gemini .
docker run -p 8001:8000 --env-file .env yolo-gemini
```
Accede a: http://localhost:8001/docs

---

## 📦 Flujo de trabajo actual

1. Subir imagen original a **POST /detect** (Módulo 1)
2. Guardar la imagen base64 como archivo **.jpg**
3. Subir **recorte.jpg** a **POST /analyze** (Módulo 2)
4. Recibir JSON con la descripción completa del vehículo

---

## 🔜 Próxima Fase (en curso)
✔️ Combinar ambos módulos en un solo microservicio:

1. Un solo POST /analyze que:
2. Detecta vehículo
3. Recorta imagen
4. Llama a Gemini

Devuelve todo el resultado automáticamente

## 🧑‍💻 Autores
Universidad Central del Ecuador
Facultad de Ingenieria y Ciencias Aplicadas
Sistemas de Informacion
Mineria de Datos
Yoshua Calahorrano y John Guerra
SIS8-001