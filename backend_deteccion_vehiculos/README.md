## Aplicacion de deteccion de vehiculos con IA Generativa

Este proyecto permite identificar vehículos a partir de imágenes y análisis generativo con Gemini 2.0 Flash. Toda la información se almacena automáticamente.

---

## 📌 Módulos del Proyecto

```bash
backend_deteccion_vehiculos/
├── Modulo_Gemini_Vehicle_Info/      # Gemini – análisis generativo
├── Modulo_Unificador_Backend/       # Orquestador principal
├── Modulo_Base/                     # Logger en MySQL
├── nginx/                           # Proxy reverso
└── docker-compose.yml               # Orquestador
```

---

## ⚙️ Tecnologías usadas

| Componente           | Tecnología                   |
| -------------------- | ---------------------------- |
| IA generativa        | Gemini 2.0 Flash (Google AI) |
| Backend              | FastAPI + Python             |
| Base de datos        | MySQL 5.7 (Docker)           |
| Contenedores         | Docker                       |
| Orquestador          | Docker Compose               |
| Servidor             | NGINX                        |

---

## 🚀 Ejecución global

```bash
docker compose up --build
```
Accede desde navegador
```bash
http://<IP PC>:8002
```

---

## 🧾 Flujo del sistema
Subir imagen
Se verifica la imagen con Gemini si existen vehiculos de la imagen.
Se analiza la imagen con Gemini.
Se guarda el resultado en MySQL.
Se retorna el JSON.

---

## 🧑‍💻 Autores
- Yoshua Calahorrano & John Guerra
- UCE – Minería de Datos – SIS8-001