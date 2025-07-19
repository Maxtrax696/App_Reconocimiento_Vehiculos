#!/bin/bash

# Ruta del proyecto (ajusta si cambiaste de directorio)
cd /home/ec2-user/backend_deteccion_vehiculos || exit

# Opcional: carga variables de entorno si tienes .env
if [ -f .env ]; then
  export $(grep -v '^#' .env | xargs)
fi

# Ejecutar servicios en modo detached
echo "🚀 Levantando contenedores..."
docker compose up -d

# Mostrar contenedores activos
echo "📦 Contenedores en ejecución:"
docker ps
