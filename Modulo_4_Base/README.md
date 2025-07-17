# Módulo 4: Logger API – Registro en Base de Datos

Este microservicio es responsable de **almacenar en una base de datos MySQL** los datos de los vehículos analizados por el sistema (marca, modelo, año, precio y reseña). Su funcionalidad se activa automáticamente desde el **Módulo 3 (unificador)**, sin necesidad de exponer endpoints REST ni ejecutar tareas manuales.

---

## 📦 Estructura del Proyecto

```bash
Modulo_4_Base/
├── app/
│ └── database.py # Conexión y lógica para guardar los datos en MySQL
├── .env # Variables de entorno para conexión a la base de datos
├── .gitignore # Archivos ignorados por Git
├── Dockerfile # Imagen Docker ligera
└── README.md # Documentación del módulo
```

---

## ⚙️ Configuración del Entorno

El archivo `.env` contiene las variables necesarias para conectarse al contenedor de la base de datos:

```env
DB_HOST=db
DB_PORT=3306
DB_NAME=vehiculos_db
DB_USER=user
DB_PASSWORD=1234
```

Estas credenciales deben coincidir con las definidas en el docker-compose.yml.

---

## 🐳 Docker
Este módulo está diseñado para ejecutarse como un contenedor ligero sin comandos expuestos, ya que actúa como dependencia del Módulo 3 (unificador).

Build de la imagen:
```bash
docker build -t proyecto_final-logger-api .
```

Uso en docker-compose.yml:
```bash
logger-api:
  build:
    context: ./Modulo_4_Base
  container_name: logger-api
  env_file:
    - ./Modulo_4_Base/.env
  networks:
    - vehiclenet
```

---

## 💾 Base de Datos
Sistema: MySQL 5.7

Contenedor: db

Tabla: vehiculos

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001