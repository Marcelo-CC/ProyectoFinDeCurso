import tkinter as tk
from tkinter import messagebox
import sqlite3
import hashlib


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def registrar_preguntas(usuario):

    def guardar_preguntas():
        pregunta_1 = entry_pregunta_1.get().strip()
        respuesta_1 = entry_respuesta_1.get().strip()
        pregunta_2 = entry_pregunta_2.get().strip()
        respuesta_2 = entry_respuesta_2.get().strip()

        if not pregunta_1 or not respuesta_1 or not pregunta_2 or not respuesta_2:
            messagebox.showerror("Error", "Por favor, llena todas las preguntas y respuestas.")
            return


        respuesta_1_hash = hashlib.sha256(respuesta_1.encode()).hexdigest()
        respuesta_2_hash = hashlib.sha256(respuesta_2.encode()).hexdigest()


        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        try:

            cursor.execute("SELECT * FROM usuarios WHERE nombre = ?", (usuario,))
            usuario_existente = cursor.fetchone()

            if usuario_existente:

                cursor.execute("""
                    UPDATE usuarios
                    SET pregunta_1 = ?, respuesta_1 = ?, pregunta_2 = ?, respuesta_2 = ?
                    WHERE nombre = ?
                """, (pregunta_1, respuesta_1_hash, pregunta_2, respuesta_2_hash, usuario))
                conexion.commit()
                messagebox.showinfo("Éxito", "Preguntas de seguridad actualizadas correctamente.")
            else:

                cursor.execute("""
                    UPDATE usuarios
                    SET pregunta_1 = ?, respuesta_1 = ?, pregunta_2 = ?, respuesta_2 = ?
                    WHERE nombre = ?
                """, (pregunta_1, respuesta_1_hash, pregunta_2, respuesta_2_hash, usuario))
                conexion.commit()
                messagebox.showinfo("Éxito", "Preguntas de seguridad registradas correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al guardar las preguntas: {str(e)}")
        finally:
            conexion.close()


    ventana = tk.Tk()
    ventana.title("Registro de Preguntas de Seguridad")
    ventana.geometry("400x400")

    tk.Label(ventana, text="Registra tus preguntas de seguridad", font=("Arial", 18)).pack(pady=10)

    tk.Label(ventana, text="Pregunta de seguridad 1:", font=("Arial", 12)).pack(pady=5)
    entry_pregunta_1 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_pregunta_1.pack(pady=5)

    tk.Label(ventana, text="Respuesta 1:", font=("Arial", 12)).pack(pady=5)
    entry_respuesta_1 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_respuesta_1.pack(pady=5)

    tk.Label(ventana, text="Pregunta de seguridad 2:", font=("Arial", 12)).pack(pady=5)
    entry_pregunta_2 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_pregunta_2.pack(pady=5)

    tk.Label(ventana, text="Respuesta 2:", font=("Arial", 12)).pack(pady=5)
    entry_respuesta_2 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_respuesta_2.pack(pady=5)

    # Botón para guardar las preguntas de seguridad
    btn_guardar = tk.Button(ventana, text="Guardar preguntas", command=guardar_preguntas, font=("Arial", 12),
                            bg="green", fg="white")
    btn_guardar.pack(pady=20)

    ventana.mainloop()


def actualizar_preguntas(usuario):

    def actualizar():
        pregunta_1 = entry_pregunta_1.get().strip()
        respuesta_1 = entry_respuesta_1.get().strip()
        pregunta_2 = entry_pregunta_2.get().strip()
        respuesta_2 = entry_respuesta_2.get().strip()

        if not pregunta_1 or not respuesta_1 or not pregunta_2 or not respuesta_2:
            messagebox.showerror("Error", "Por favor, llena todas las preguntas y respuestas.")
            return


        respuesta_1_hash = hashlib.sha256(respuesta_1.encode()).hexdigest()
        respuesta_2_hash = hashlib.sha256(respuesta_2.encode()).hexdigest()


        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        try:

            cursor.execute("""
                UPDATE usuarios
                SET pregunta_1 = ?, respuesta_1 = ?, pregunta_2 = ?, respuesta_2 = ?
                WHERE nombre = ?
            """, (pregunta_1, respuesta_1_hash, pregunta_2, respuesta_2_hash, usuario))
            conexion.commit()
            messagebox.showinfo("Éxito", "Preguntas de seguridad actualizadas correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un error al actualizar las preguntas: {str(e)}")
        finally:
            conexion.close()


    ventana = tk.Tk()
    ventana.title("Actualizar Preguntas de Seguridad")
    ventana.geometry("400x400")

    tk.Label(ventana, text="Actualiza tus preguntas de seguridad", font=("Arial", 18)).pack(pady=10)

    tk.Label(ventana, text="Pregunta de seguridad 1:", font=("Arial", 12)).pack(pady=5)
    entry_pregunta_1 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_pregunta_1.pack(pady=5)

    tk.Label(ventana, text="Respuesta 1:", font=("Arial", 12)).pack(pady=5)
    entry_respuesta_1 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_respuesta_1.pack(pady=5)

    tk.Label(ventana, text="Pregunta de seguridad 2:", font=("Arial", 12)).pack(pady=5)
    entry_pregunta_2 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_pregunta_2.pack(pady=5)

    tk.Label(ventana, text="Respuesta 2:", font=("Arial", 12)).pack(pady=5)
    entry_respuesta_2 = tk.Entry(ventana, width=40, font=("Arial", 12))
    entry_respuesta_2.pack(pady=5)


    btn_actualizar = tk.Button(ventana, text="Actualizar preguntas", command=actualizar, font=("Arial", 12),
                               bg="green", fg="white")
    btn_actualizar.pack(pady=20)

    ventana.mainloop()
