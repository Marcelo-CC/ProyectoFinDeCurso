import sqlite3
from tkinter import messagebox
from src.logica.iniciar_sesion import hash_password

def actualizar_contrasena(nombre_usuario, nueva_contrasena):
    hashed_password = hash_password(nueva_contrasena)

    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "UPDATE usuarios SET contrasena = ? WHERE nombre = ?",
            (hashed_password, nombre_usuario)
        )
        conexion.commit()

        if cursor.rowcount > 0:
            print("Contraseña actualizada correctamente.")
        else:
            print("No se encontró el usuario.")
    except sqlite3.Error as e:
        print(f"Error al actualizar la contraseña: {e}")
    finally:
        conexion.close()