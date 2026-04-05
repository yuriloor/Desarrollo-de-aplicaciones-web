import sqlite3

def crear_bd():
    conexion = sqlite3.connect('inventario.db')
    cursor = conexion.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT,
            cantidad INTEGER,
            precio REAL
        )
    ''')

    conexion.commit()
    conexion.close()

# Ejecutar creación
crear_bd()