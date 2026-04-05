from flask import Flask, render_template, request, redirect, send_file, jsonify
from flask_sqlalchemy import SQLAlchemy
import json, os, csv

app = Flask(__name__)

# =========================
# 🔥 CONFIGURACIÓN MYSQL (XAMPP)
# =========================
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:@localhost/inventario'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# =========================
# MODELO
# =========================
class Producto(db.Model):
    __tablename__ = 'productos'

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100))
    cantidad = db.Column(db.Integer)
    precio = db.Column(db.Float)

# =========================
# CREAR TABLA (SI NO EXISTE)
# =========================
with app.app_context():
    db.create_all()

# =========================
# INICIO
# =========================
@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/clientes')
def clientes():
    return render_template('clientes.html')

# =========================
# MOSTRAR PRODUCTOS
# =========================
@app.route('/productos')
def productos():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

# =========================
# AGREGAR PRODUCTO
# =========================
@app.route('/agregar', methods=['POST'])
def agregar():
    nombre = request.form['nombre']
    cantidad = request.form['cantidad']
    precio = request.form['precio']

    nuevo = Producto(
        nombre=nombre,
        cantidad=int(cantidad),
        precio=float(precio)
    )
    db.session.add(nuevo)
    db.session.commit()

    # TXT
    os.makedirs('inventario/data', exist_ok=True)
    with open('inventario/data/datos.txt', 'a') as archivo:
        archivo.write(f"{nombre},{cantidad},{precio}\n")

    # JSON
    ruta_json = 'inventario/data/datos.json'

    if not os.path.exists(ruta_json):
        with open(ruta_json, 'w') as archivo:
            json.dump([], archivo)

    try:
        with open(ruta_json, 'r') as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    datos.append({
        "nombre": nombre,
        "cantidad": cantidad,
        "precio": precio
    })

    with open(ruta_json, 'w') as archivo:
        json.dump(datos, archivo, indent=4)

    # CSV
    ruta_csv = 'inventario/data/datos.csv'

    if not os.path.exists(ruta_csv):
        with open(ruta_csv, 'w', newline='') as archivo:
            writer = csv.writer(archivo)
            writer.writerow(['nombre', 'cantidad', 'precio'])

    with open(ruta_csv, 'a', newline='') as archivo:
        writer = csv.writer(archivo)
        writer.writerow([nombre, cantidad, precio])

    return redirect('/productos')

# =========================
# ELIMINAR PRODUCTO
# =========================
@app.route('/eliminar/<int:id>')
def eliminar(id):
    producto = Producto.query.get(id)
    if producto:
        db.session.delete(producto)
        db.session.commit()
    return redirect('/productos')

# =========================
# BUSCAR
# =========================
@app.route('/buscar', methods=['POST'])
def buscar():
    nombre = request.form['nombre']

    productos = Producto.query.filter(
        Producto.nombre.like(f"%{nombre}%")
    ).all()

    return render_template('productos.html', productos=productos)

# =========================
# 🔍 AUTOCOMPLETE
# =========================
@app.route('/autocomplete')
def autocomplete():
    texto = request.args.get('q')

    productos = Producto.query.filter(
        Producto.nombre.like(f"%{texto}%")
    ).all()

    resultados = [p.nombre for p in productos]

    return jsonify(resultados)

# =========================
# VER JSON
# =========================
@app.route('/ver_json')
def ver_json():
    with open('inventario/data/datos.json', 'r') as archivo:
        datos = json.load(archivo)

    return render_template('datos.html', datos=datos)

# =========================
# VER CSV
# =========================
@app.route('/ver_csv')
def ver_csv():
    datos = []

    with open('inventario/data/datos.csv', 'r') as archivo:
        reader = csv.reader(archivo)
        next(reader)

        for fila in reader:
            datos.append({
                "nombre": fila[0],
                "cantidad": fila[1],
                "precio": fila[2]
            })

    return render_template('datos.html', datos=datos)

# =========================
# DESCARGAS
# =========================
@app.route('/descargar_txt')
def descargar_txt():
    return send_file('inventario/data/datos.txt', as_attachment=True)

@app.route('/descargar_json')
def descargar_json():
    return send_file('inventario/data/datos.json', as_attachment=True)

@app.route('/descargar_csv')
def descargar_csv():
    return send_file('inventario/data/datos.csv', as_attachment=True)

# =========================
# EJECUTAR
# =========================
if __name__ == '__main__':
    app.run(debug=True)