import mysql.connector

def save_vehicle_data(marca, modelo, year, precio, detalles):
    conn = None
    try:
        conn = mysql.connector.connect(
            host="db",
            user="user",
            password="1234",
            database="vehiculos_db"
        )
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO vehiculos (marca, modelo, year, precio, detalles)
            VALUES (%s, %s, %s, %s, %s)
        """
        cursor.execute(insert_query, (marca, modelo, year, precio, detalles))
        conn.commit()
        print("✅ Datos guardados exitosamente.")
    except mysql.connector.Error as err:
        print(f"❌ Error al guardar los datos: {err}")
    finally:
        if conn:
            conn.close()

