from flask import Flask, render_template, request, url_for, redirect
# from flask_mysqldb import MySQL
from flaskext.mysql import MySQL
import pymysql
import pymysql.cursors

app = Flask(__name__) 

# ---------------------------------------------------------------------------------------

# Configurar conexion a base de datos
# app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'felipe'
app.config['MYSQL_DATABASE_DB'] = 'vacunatorio'

# Iniciar la conexion MYSQL
mysql = MySQL(app)
mysql.connect_args["autocommit"] = True
mysql.connect_args["cursorclass"] = pymysql.cursors.DictCursor

# ---------------------------------------------------------------------------------------

# Ruta inicial, listar todos los pacientes registrados
@app.route('/')
def Index():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT rut, nombre, date_format(fecha_nacimiento, '%d-%m-%Y') as fecha_nacimiento FROM Paciente")
    data = cursor.fetchall()

    return render_template("index.html", pacientes = data)

# ---------------------------------------------------------------------------------------

# Ruta para agregar pacientes
@app.route('/paciente/add', methods=["GET", "POST"])
def add_paciente():
    if request.method == "GET":
        return render_template("nuevoPaciente.html")

    if request.method == "POST":
        rut = request.form["rut"]
        nombre = request.form["nombre"]
        fechaNacimiento = request.form["fechaNacimiento"]

        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT rut FROM Paciente WHERE rut = %s", (rut))
        ruts = cursor.fetchall()
        if len(ruts) > 0:
            return redirect(url_for("Index"))
        else:
            sql = "INSERT INTO Paciente (rut, nombre, fecha_nacimiento) VALUES (%s, %s, %s)"
            cursor.execute(sql, (rut, nombre, fechaNacimiento))
            return redirect(url_for("Index"))

# ---------------------------------------------------------------------------------------

#Ruta para registra vacuna a paciente
@app.route('/paciente/<string:rut>/addVacuna', methods=["GET", "POST"])
def add_vacuna_paciente(rut):
    if request.method == "GET":
        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT * FROM Paciente WHERE rut = %s', (rut))
        data = cursor.fetchall()
        cursor.execute("SELECT * FROM Vacuna")
        vacunas = cursor.fetchall()

        return render_template("vacunarPaciente.html", paciente = data[0], vacunas = vacunas)

    if request.method == "POST":
        vacuna = request.form["vacuna"]

        # Si no existen vacunas registradas o no se ha seleccionado vacuna, no hacer nada y redireccionar al index
        if vacuna == "-1":
           return redirect(url_for("Index"))

        sql = "INSERT INTO Recibe (rut_paciente, nombre_enfermedad) VALUES (%s, %s)"
        cursor = mysql.get_db().cursor()
        cursor.execute(sql, (rut, vacuna))
        return redirect(url_for("Index"))

# ---------------------------------------------------------------------------------------

# Ruta para agregar vacunas
@app.route('/vacuna/add', methods=["GET", "POST"])
def add_vacuna():
    if request.method == "GET":
        return render_template("nuevaVacuna.html")

    if request.method == "POST":
        enfermedad = request.form["enfermedad"]
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT nombre_enfermedad FROM Vacuna WHERE nombre_enfermedad = %s", (enfermedad))
        enfermedades = cursor.fetchall()
        if len(enfermedades) > 0:
            return redirect(url_for("listar_vacunas"))
        else:
            sql = "INSERT INTO Vacuna (nombre_enfermedad) VALUES (%s)"
            cursor.execute(sql, (enfermedad))
            return redirect(url_for("listar_vacunas"))

# ---------------------------------------------------------------------------------------

# Ruta para listar todas las vacunas registradas
@app.route('/vacunas')
def listar_vacunas():
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT nombre_enfermedad, date_format(fecha_registro, '%d-%m-%Y') as fecha_registro FROM Vacuna")
    data = cursor.fetchall()

    return render_template("listarVacunas.html", vacunas = data)

# ---------------------------------------------------------------------------------------

# Ruta para listar todos los pacientes vacunados contra una enfermedad 
@app.route('/vacunas/<string:enfermedad>/pacientes')
def listar_pacientes_vacunados(enfermedad):
    cursor = mysql.get_db().cursor()
    sql = 'SELECT p.nombre, p.rut, r.fecha_vacuna FROM Recibe r INNER JOIN Paciente p ON r.rut_paciente = p.rut INNER JOIN Vacuna v ON r.nombre_enfermedad = v.nombre_enfermedad WHERE v.nombre_enfermedad = %s';
    cursor.execute(sql, (enfermedad))
    data = cursor.fetchall()

    return render_template("listarPacientesVacunados.html", vacunas = data, nombreEnfermedad = enfermedad)

# ---------------------------------------------------------------------------------------

# Ruta para listar todas las vacunas de un paciente
@app.route('/paciente/<string:rut>/vacunas')
def listar_vacunas_paciente(rut):
    cursor = mysql.get_db().cursor()
    sql = 'SELECT p.nombre, v.nombre_enfermedad, r.fecha_vacuna FROM Recibe r INNER JOIN Paciente p ON r.rut_paciente = p.rut INNER JOIN Vacuna v ON r.nombre_enfermedad = v.nombre_enfermedad WHERE p.rut = %s';
    cursor.execute(sql, (rut))
    data = cursor.fetchall()
    cursor.execute("SELECT nombre FROM Paciente WHERE rut = %s", (rut))
    nombrePaciente = cursor.fetchall()
    return render_template("listarVacunasPaciente.html", vacunas = data, nombre_paciente = nombrePaciente[0]["nombre"])

# ---------------------------------------------------------------------------------------

if __name__ == "__main__":
    app.run(port = 3000, debug = True)