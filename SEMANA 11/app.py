from flask import Flask, render_template, request, redirect
import sqlite3
from database import crear_tabla

app = Flask(__name__)

crear_tabla()

def conectar():
    return sqlite3.connect("inventario.db")

@app.route("/")
def inicio():
    return render_template("index.html")

@app.route("/productos")
def productos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    datos = cursor.fetchall()
    conn.close()
    return render_template("productos.html", productos=datos)

@app.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        nombre = request.form["nombre"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        conn = conectar()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO productos (nombre, cantidad, precio) VALUES (?, ?, ?)",
                       (nombre, cantidad, precio))
        conn.commit()
        conn.close()

        return redirect("/productos")

    return render_template("agregar.html")

@app.route("/eliminar/<int:id>")
def eliminar(id):
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM productos WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/productos")

if __name__ == "__main__":
    app.run(debug=True)