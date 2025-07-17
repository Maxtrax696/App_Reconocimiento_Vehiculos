# Imagen base de Python
FROM python:3.10-slim

# Establecemos el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiamos los archivos necesarios
COPY app/ app/
COPY .env .env

# Instalamos las dependencias necesarias
RUN pip install mysql-connector-python python-dotenv

# El contenedor no necesita ejecutar nada por sí solo
# Ya que es llamado como librería desde el Módulo 3
# Por lo tanto, no definimos CMD ni EXPOSE