# Importa las librerías necesarias
from flask import Flask, render_template
import pyodbc

# Crea una instancia de la aplicación Flask
app = Flask(__name__)

# Configura la conexión a la base de datos Access
db_connection = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                               r'DBQ=C:\Users\Camilo\Documents\Parcial01\TallerDB.accdb;')

# Define una ruta para la página de inicio
@app.route('/')
def inicio():
    return "¡Bienvenido a la aplicación de TallerDB de Camilo Arambula"

# Define una ruta para listar estudiantes desde la base de datos
@app.route('/estudiantes')
def listar_estudiantes():
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM Estudiantes')
    estudiantes = cursor.fetchall()
    return render_template('estudiantes.html', estudiantes=estudiantes)

# Define una ruta para listar cursos desde la base de datos
@app.route('/cursos')
def listar_cursos():
    cursor = db_connection.cursor()
    cursor.execute('SELECT * FROM cursos')
    cursos = cursor.fetchall()
    return render_template('cursos.html', cursos=cursos)

# Punto de entrada para ejecutar la aplicación si se ejecuta directamente desde este archivo.
if __name__ == '__main__':
    app.run(debug=True) 


    
