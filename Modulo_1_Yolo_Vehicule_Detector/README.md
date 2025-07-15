## Modulo 1

## 🧠 ¿Qué hace este servicio?

1. Recibe una imagen (JPG o PNG) enviada por POST.
2. Utiliza **YOLOv8** para detectar el vehículo en la imagen.
3. Recorta la región del vehículo detectado.
4. Devuelve la imagen recortada en formato **Base64** (ideal para consumir desde una app móvil).

---

## 🧱 Tecnologías utilizadas

- Python 3.10
- FastAPI
- OpenCV + Pillow
- Ultralytics YOLOv8
- Docker (para empaquetado)

---

## Estructura del modulo 1

```bash
Modulo_1_Yolo-Vehicule-Detector/
├── app/
│   ├── detection.py          # lógica de YOLO
│   ├── utils.py              # funciones auxiliares
│   └── guardar_recorte.py    # guarda la imagen recortada
├── main.py                   # API REST con FastAPI
├── requirements.txt          # librerías necesarias
├── Dockerfile                # contenedor opcional
├── .gitignore
└── README.md
```

## 🚀 Cómo ejecutar con Docker

```bash
# Construir imagen
docker build -t yolo-detector .

# Ejecutar contenedor
docker run -p 8000:8000 yolo-detector
```

## 🧑‍💻 Autores
Universidad Central del Ecuador
Facultad de Ingenieria y Ciencias Aplicadas
Sistemas de Informacion
Mineria de Datos
Yoshua Calahorrano y John Guerra
SIS8-001