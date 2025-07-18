# Frontend – Identificador de Vehículos 🚗📱

Este es el frontend del sistema de identificación de vehículos usando IA generativa y visión por computadora. Permite a los usuarios subir una imagen desde su celular o PC, visualizar los resultados generados por el backend y consultar un historial local de búsquedas anteriores.

---

## 🧱 Estructura
```bash
frontend/
├── index.html # Página principal
├── historial.html # Página de historial local
├── style.css # Estilos personalizados (Bootstrap)
├── script.js # Lógica del análisis
├── historial.js # Lógica del historial + descarga
```


---

## 🧰 Tecnologías utilizadas

- HTML5 + CSS3
- Bootstrap 5.3
- JavaScript puro
- LocalStorage (para historial)
- html2canvas (para descargar tarjetas como imágenes)

---

## ⚙️ ¿Cómo funciona?

1. El usuario selecciona una imagen (JPG o PNG)
2. El frontend hace un `POST /analyze` al backend
3. Se muestran los resultados:
   - Marca
   - Modelo
   - Año
   - Precio estimado
   - Reseña del vehículo
4. La imagen recortada también se muestra
5. Los datos se almacenan en el historial local del navegador

---

## 📦 Requisitos

Este frontend debe ser servido desde un servidor (por ejemplo, NGINX en el contenedor `frontend-nginx`) para que las peticiones funcionen correctamente.

Evita abrir `index.html` directamente desde el explorador (con `file://`), ya que las rutas relativas no funcionarán correctamente.

---

## 🛠️ Cómo acceder desde otras PCs o celulares

1. Asegúrate de que `docker-compose up` esté corriendo en la máquina principal
2. Desde otro dispositivo conectado a la misma red, abre el navegador en:

http://<IP-de-la-PC-principal>

3. ¡Listo! Ya puedes analizar imágenes desde otros dispositivos sin configurar rutas manuales

---

## 🖼️ Historial y exportación

El historial se guarda automáticamente en el navegador del usuario (LocalStorage). También puedes:

- Visualizar búsquedas anteriores en `historial.html`
- Descargar tarjetas individuales como imágenes JPG

---

## 🧑‍💻 Autores
- Universidad Central del Ecuador
- Facultad de Ingenieria y Ciencias Aplicadas
- Sistemas de Informacion
- Mineria de Datos
- Yoshua Calahorrano y John Guerra
- SIS8-001