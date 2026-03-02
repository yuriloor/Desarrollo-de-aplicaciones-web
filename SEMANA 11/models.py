class Producto:
    def __init__(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def get_datos(self):
        return (self.id, self.nombre, self.cantidad, self.precio)


class Inventario:
    def __init__(self):
        self.productos = {}  # Diccionario {id: Producto}

    def agregar_producto(self, producto):
        self.productos[producto.id] = producto

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad:
                self.productos[id].cantidad = cantidad
            if precio:
                self.productos[id].precio = precio

    def buscar_por_nombre(self, nombre):
        return [p for p in self.productos.values() if nombre.lower() in p.nombre.lower()]

    def mostrar_todos(self):
        return list(self.productos.values())