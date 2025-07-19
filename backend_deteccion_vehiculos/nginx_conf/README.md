# NGINX – Servidor para Frontend + Proxy para Backend

Este contenedor NGINX cumple una doble función:

1. Redirigir automáticamente `/analyze` al microservicio `unified-api` (backend FastAPI)

---

## 📁 Estructura

```bash
nginx_conf/
└── default.conf # Configuración principal del servidor
```

---

## ⚙️ Configuración (default.conf)

```nginx
server {
    listen 80;
    server_name _;

    client_max_body_size 10M;

    # Redirige /analyze al backend real (FastAPI puerto 8002)
    location /analyze {
        proxy_pass http://unified-api:8000/analyze;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    # Ruta raíz muestra texto plano
    location / {
        default_type text/plain;
        add_header Content-Type "text/plain; charset=utf-8";
        return 200 "🚗 Servidor NGINX en ejecución para el Detector de Vehículos 🚗\n";
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

Debería mostrar el mensaje de confirmacion del servidor.

---

## 🧯 Problemas comunes
- 413 Entity too large → Solución: aumentar client_max_body_size como se muestra arriba

- Error 502 → Asegúrate de que el backend esté corriendo y accesible como unified-api:8000 dentro de la red Docker

---

## 🧑‍💻 Autores
- Yoshua Calahorrano & John Guerra
- UCE – Minería de Datos – SIS8-0011