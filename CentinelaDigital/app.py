from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Configuración de la conexión a la base de datos (XAMPP / MySQL)
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",          # Por defecto en XAMPP va vacío
        database="centinela_digital"
    )

@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/reportar")
def reportar():
    return render_template("reportar.html")


@app.route("/guardar", methods=["POST"])
def guardar():

    try:

        print("ENTRÓ AL GUARDAR")

        nombre = request.form["nombre"]
        institucion = request.form["institucion"]
        tipo = request.form["tipo"]
        descripcion = request.form["descripcion"]

        conexion = obtener_conexion()

        cursor = conexion.cursor()

        sql = """
        INSERT INTO reporte 
        (nombre, tipo_violencia, institucion, descripcion)
        VALUES (%s, %s, %s, %s)
        """

        datos = (
            nombre,
            tipo,
            institucion,
            descripcion
        )

        cursor.execute(sql, datos)

        conexion.commit()

        cursor.close()
        conexion.close()

        print("Datos guardados correctamente")

        return render_template("exitoso.html")


    except Exception as e:

        print("ERROR:", e)

        return "Error: " + str(e)


@app.route("/violencia")
def violencia():
    return render_template("tipos-violencia.html")


@app.route("/instituciones")
def instituciones():
    return render_template("instituciones.html")


@app.route("/contacto")
def contacto():
    return render_template("contacto.html")


if __name__ == "__main__":
    app.run(debug=True)