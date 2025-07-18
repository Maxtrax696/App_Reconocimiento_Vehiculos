# NGINX – Servidor para Frontend + Proxy para Backend

Este contenedor NGINX cumple una doble función:

1. Servir el frontend (`index.html`) a través del puerto `80`
2. Redirigir automáticamente `/analyze` al microservicio `unified-api` (backend FastAPI)

---

## 📁 Estructura

```bash
nginx/
└── default.conf # Configuración principal del servidor
```

---

## ⚙️ Configuración (default.conf)

```nginx
server {
    listen 80;
    server_name _;

    client_max_body_size 10M;  # Aumenta el tamaño permitido para subir imágenes

    root /usr/share/nginx/html;
    index index.html;

    location / {
        try_files $uri $uri/ /index.html;
    }

    location /analyze {
        proxy_pass http://unified-api:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }
}
```

---

## 🔌 Requisitos de red
Asegúrate de que:
    - El contenedor NGINX (frontend-nginx) y el backend (unified-api) estén en la misma red Docker (vehiclenet)
    - El backend escuche en el puerto 8000 internamente
    - El contenedor NGINX exponga el puerto 80 externamente ("80:80")

---

## 🧪 Prueba de funcionamiento
Desde el navegador de cualquier dispositivo en la red:

```bash
http://<IP-local-de-la-PC>
```

Debería mostrar el frontend.
El análisis funcionará automáticamente al enviar imágenes a /analyze.

---

## 🧯 Problemas comunes
- 413 Entity too large → Solución: aumentar client_max_body_size como se muestra arriba

- CORS → No aplica si el frontend y backend están en la misma IP/dominio

- Error 502 → Asegúrate de que el backend esté corriendo y accesible como unified-api:8000 dentro de la red Docker

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001