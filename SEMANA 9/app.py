from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return "Bienvenido al Sistema de Inventario — Gestión de equipos"

@app.route('/item/<codigo>')
def item(codigo):
    return f"Item {codigo} registrado correctamente."

if __name__ == '__main__':
    app.run(debug=True)
