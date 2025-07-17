import mysql.connector

def save_vehicle_data(marca, modelo, precio, detalles):
    """Función para guardar los datos de un vehículo en la base de datos"""
    conn = None  # Inicializamos la variable conn

    try:
        # Conexión a la base de datos MySQL
        conn = mysql.connector.connect(
            host="db",  # Nombre del servicio de MySQL en Docker
            user="user",  # Usuario configurado en Docker
            password="1234",  # Contraseña configurada en Docker
            database="vehiculos_db"  # Nombre de la base de datos
        )
        cursor = conn.cursor()

        # Consulta para insertar los datos en la tabla vehiculos (sin necesidad de `id`)
        insert_query = """
            INSERT INTO vehiculos (marca, modelo, precio, detalles)
            VALUES (%s, %s, %s, %s)
        """
        cursor.execute(insert_query, (marca, modelo, precio, detalles))

        # Confirmar la transacción
        conn.commit()

        print("Datos guardados exitosamente.")

    except mysql.connector.Error as err:
        # Si hay un error, lo mostramos
        print(f"Error al guardar los datos: {err}")

    finally:
        # Asegurarnos de cerrar la conexión solo si se creó correctamente
        if conn:
            conn.close()  # Cerrar la conexión
