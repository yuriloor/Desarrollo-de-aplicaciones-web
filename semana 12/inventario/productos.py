import json
import csv

# Guardar en TXT
def guardar_txt(producto):

    with open("inventario/data/datos.txt", "a") as archivo:
        archivo.write(f"{producto['nombre']},{producto['precio']},{producto['cantidad']}\n")


# Guardar en JSON
def guardar_json(producto):

    ruta = "inventario/data/datos.json"

    try:
        with open(ruta, "r") as archivo:
            datos = json.load(archivo)
    except:
        datos = []

    datos.append(producto)

    with open(ruta, "w") as archivo:
        json.dump(datos, archivo, indent=4)


# Guardar en CSV
def guardar_csv(producto):

    with open("inventario/data/datos.csv", "a", newline="") as archivo:

        writer = csv.writer(archivo)

        writer.writerow([
            producto["nombre"],
            producto["precio"],
            producto["cantidad"]
        ])