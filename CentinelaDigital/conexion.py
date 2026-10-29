import mysql.connector


try:

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="centinela_digital"
    )


    if conexion.is_connected():
        print("✅ Conexión exitosa a la base de datos")


    conexion.close()
    print("Conexión cerrada correctamente")


except mysql.connector.Error as error:

    print("❌ Error de conexión:")
    print(error) 