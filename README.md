## Aplicacion movil de detecteccion de vehiculos con IA Generativa (LLM)

Aplicacion instalable para dispositivos moviles Android por APK, para ingresar imagen de galeria o camara directamente para detectar marca, modelo, ano, precio y datelles del vehiculo como tal.

---

## Estructura del proyecto
```bash
PROYECTO_FINAL/
|__ backend_deteccion_Vehiculos/    # Codificacion de programa dockerizado y con Nginx
|__ vehicule_detector_app/          # Codificacion de frontend aplicacion movil con **flutter** para Android
|__ README.md
```

---

## Flujo
1. Aplicacion se conecta directamente con la direccion del contenedor unifier-api/analyze a la <IP_de_PC>
2. Envia imagen tomada por usuario para realizar las validacion y analisis.
3. Retorna respuesta y se visualiza la informacion del resultado
4. Se guarda un historial de los resultados del dispositivo

---

## Instalacion de APK
1. Activar instalacion de aplicaciones externas en dispositivo movil
2. Instalar APK de aplicacion
3. Debe estar conectado a la red de la ip/contenedor.
4. Listo!, disfruta de la aplicacion

---

## 🧑‍💻 Autores
- Yoshua Calahorrano & John Guerra
- UCE – Minería de Datos – SIS8-001