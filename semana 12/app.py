from flask import Flask, render_template, request, redirect
from inventario.bd import db, Producto
from inventario.productos import guardar_txt, guardar_json, guardar_csv

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///inventario.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/guardar", methods=["POST"])
def guardar():

    nombre = request.form["nombre"]
    precio = request.form["precio"]
    cantidad = request.form["cantidad"]

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    guardar_txt(producto)
    guardar_json(producto)
    guardar_csv(producto)

    nuevo = Producto(nombre=nombre, precio=precio, cantidad=cantidad)

    db.session.add(nuevo)
    db.session.commit()

    return redirect("/")