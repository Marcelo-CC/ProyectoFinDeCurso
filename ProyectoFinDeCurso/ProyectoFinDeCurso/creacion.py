import sqlite3

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

try:
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contrasenas_servicios (
            servicio TEXT NOT NULL,
            usuario TEXT NOT NULL,
            contrasena TEXT NOT NULL
        )
    """)
    conexion.commit()
    print("Tabla 'contrasenas_servicios' creada correctamente.")
finally:
    conexion.close()