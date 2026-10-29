from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)


@app.route("/")
def inicio():
    return render_template("index.html")


@app.route("/reportar")
def reportar():
    return render_template("reportar.html")


@app.route("/exitoso", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    institucion = request.form["institucion"]
    tipo = request.form["tipo"]
    descripcion = request.form["descripcion"]

    conexion = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="centinela_digital"
    )

    cursor = conexion.cursor()

    sql = """
    INSERT INTO reporte
    (nombre, institucion, tipo_violencia, descripcion)
    VALUES (%s, %s, %s, %s)
    """

    datos = (
        nombre,
        institucion,
        tipo,
        descripcion
    )

    cursor.execute(sql, datos)

    conexion.commit()

    cursor.close()
    conexion.close()

    return render_template("exitoso.html")


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