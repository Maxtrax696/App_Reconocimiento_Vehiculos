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
4. Finalmente, los resultados son guardados automáticamente en **MySQL** a través de un microservicio adicional.

---

## Link de repositorio GitHub
https://github.com/Maxtrax696/App_Reconocimiento_Vehiculos

---

## 🧱 Arquitectura por módulos

```bash
PROYECTO_FINAL/
├── Modulo_1_Yolo_Vehicule_Detector/ # Microservicio YOLOv8 para recorte de imagen
├── Modulo_2_Gemini_Vehicle_Info/ # Microservicio Gemini para inferencia de vehículo
├── Modulo_3_Unificador_Backend/ # Microservicio orquestador de los anteriores
├── Modulo_4_Base/ # Microservicio logger para guardar resultados en MySQL
├── docker-compose.yml # Orquestador general
├── data/ # Carpeta para persistencia de MySQL
└── docs/ # Documentación adicional
```

## ⚙️ Tecnologías utilizadas

| Componente           | Tecnología                   |
| -------------------- | ---------------------------- |
| Backend REST         | Python + FastAPI             |
| Visión computacional | YOLOv8 (`ultralytics`)       |
| IA generativa        | Gemini 2.0 Flash (Google AI) |
| Base de datos        | MySQL 5.7 (Docker)           |
| Contenedores         | Docker                       |
| Orquestación         | Docker Compose               |
| Comunicación         | API REST (JSON + Imágenes)   |

---

## 📦 Flujo de trabajo automatizado

1. Cliente móvil captura imagen y la envía al endpoint /analyze (Módulo 3)

2. Módulo 3 llama internamente:
   a) YOLOv8 (Módulo 1) → devuelve imagen recortada
   b) Gemini (Módulo 2) → analiza imagen y devuelve marca, modelo, etc.
   c) Logger (Módulo 4) → guarda resultados en MySQL automáticamente

3. Cliente recibe la respuesta final en JSON

---

## 🧾 Estructura de datos almacenados en MySQL

| Campo     | Tipo     | Descripción                                      |
|-----------|----------|--------------------------------------------------|
| id        | INT      | Identificador único (autoincremental)            |
| marca     | VARCHAR  | Marca del vehículo detectado                     |
| modelo    | VARCHAR  | Modelo del vehículo                              |
| precio    | VARCHAR  | Precio aproximado estimado por Gemini            |
| resena    | TEXT     | Reseña generada por IA sobre funcionalidad/uso   |

---

## 🚀 Cómo levantar el sistema con Docker Compose

### Requisitos:

- Tener creado un archivo `.env` dentro de `Modulo_2_Gemini_Vehicle_Info/` con tu API Key:

```env
GEMINI_API_KEY=tu_api_key_aqui
```

```bash
docker compose up --build
```

Esto levantará automáticamente:
- yolo-detector en http://localhost:8000
- gemini-analyzer en http://localhost:8001
- unified-api en http://localhost:8002

Esto levantará automáticamente:

   * yolo-detector en → http://localhost:8000
   * gemini-analyzer en → http://localhost:8001
   * unified-api en → http://localhost:8002
   * logger-api (sin puerto expuesto directamente)
   * db (persistente en ./data/mysql)

---

Prueba el endpoint en:
📍 http://localhost:8002/docs

---

## 🛢️ Ver datos guardados en MySQL (opcional)
Puedes ingresar al contenedor de la base de datos con:

```bash
docker exec -it db mysql -u root -p
# Contraseña: 1234
```

Luego ejecutar:
```bash
USE vehiculos_db;
SELECT * FROM vehiculos;
```

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001