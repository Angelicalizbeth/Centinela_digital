from flask import Flask, render_template, request
import mysql.connector


app = Flask(__name__)


# Página principal
@app.route("/")
def inicio():
    return render_template("index.html")


# Formulario de reporte
@app.route("/reportar")
def reportar():
    return render_template("reportar.html")


# Guardar información en la base de datos
@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    institucion = request.form["institucion"]
    tipo = request.form["tipo"]
    descripcion = request.form["descripcion"]


    try:

        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="centinela_digital"
        )


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


        return render_template("exitoso.html")


    except Exception as error:

        return "Error al guardar: " + str(error)



# Otras páginas
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