import sqlite3
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import filedialog, messagebox
import random
import string
import subprocess

from main_aplicacion import iniciar_aplicacion



def obtener_contraseñas():
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("SELECT servicio, usuario, contrasena FROM contrasenas_servicios")
        return cursor.fetchall()  # Devuelve una lista de tuplas (servicio, usuario, contrasena)
    except sqlite3.Error as e:
        print(f"Error al obtener contraseñas: {e}")
        return []
    finally:
        conexion.close()



def agregar_contraseña(servicio, usuario, contrasena):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "INSERT INTO contrasenas_servicios (servicio, usuario, contrasena) VALUES (?, ?, ?)",
            (servicio, usuario, contrasena)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "La contraseña se añadió correctamente.")
    except sqlite3.Error as e:
        print(f"Error al agregar la contraseña: {e}")
        messagebox.showerror("Error", "No se pudo agregar la contraseña.")
    finally:
        conexion.close()



def actualizar_contraseña(servicio, nueva_contraseña):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    try:
        cursor.execute(
            "UPDATE contrasenas_servicios SET contrasena = ? WHERE servicio = ?",
            (nueva_contraseña, servicio)
        )
        conexion.commit()
        messagebox.showinfo("Éxito", "La contraseña se actualizó correctamente.")
    except sqlite3.Error as e:
        print(f"Error al actualizar la contraseña: {e}")
        messagebox.showerror("Error", "No se pudo actualizar la contraseña.")
    finally:
        conexion.close()



def eliminar_contraseña(servicio):
    conexion = sqlite3.connect("usuarios.db")
    cursor = conexion.cursor()

    try:
        cursor.execute("DELETE FROM contrasenas_servicios WHERE servicio = ?", (servicio,))
        conexion.commit()
        messagebox.showinfo("Éxito", "La contraseña se eliminó correctamente.")
    except sqlite3.Error as e:
        print(f"Error al eliminar la contraseña: {e}")
        messagebox.showerror("Error", "No se pudo eliminar la contraseña.")
    finally:
        conexion.close()



def generar_contrasena_segura(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena



def iniciar_ventana_seguridad(nombre_usuario):
    ventana_seguridad = tk.Tk()
    ventana_seguridad.title("Gestión de Contraseñas")
    ventana_seguridad.geometry("600x400")


    def actualizar_lista():
        for widget in frame_lista.winfo_children():
            widget.destroy()

        contraseñas = obtener_contraseñas()
        for i, (servicio, usuario, contrasena) in enumerate(contraseñas):
            tk.Label(frame_lista, text=servicio).grid(row=i, column=0, padx=5, pady=5)
            tk.Button(frame_lista, text="Editar", command=lambda s=servicio: editar_contraseña(s)).grid(row=i, column=1)
            tk.Button(frame_lista, text="Eliminar", command=lambda s=servicio: eliminar_contraseña_interfaz(s)).grid(
                row=i, column=2)
            tk.Button(frame_lista, text="Detalles",
                      command=lambda s=servicio, u=usuario, c=contrasena: ver_detalles(s, u, c)).grid(row=i, column=3)


    def editar_contraseña(servicio):
        nueva_contraseña = simpledialog.askstring("Editar Contraseña", f"Nueva contraseña para {servicio}:")
        if nueva_contraseña:
            actualizar_contraseña(servicio, nueva_contraseña)
            actualizar_lista()


    def eliminar_contraseña_interfaz(servicio):
        respuesta = messagebox.askyesno("Eliminar Contraseña",
                                        f"¿Estás seguro de eliminar la contraseña para {servicio}?")
        if respuesta:
            eliminar_contraseña(servicio)
            actualizar_lista()


    def ver_detalles(servicio, usuario, contrasena):
        messagebox.showinfo(
            "Detalles de la Contraseña",
            f"Servicio: {servicio}\nUsuario: {usuario}\nContraseña: {contrasena}"
        )


    def generar_contraseña():
        servicio = simpledialog.askstring("Nuevo Servicio", "Nombre del servicio:", parent=ventana_seguridad)
        usuario = simpledialog.askstring("Nuevo Usuario", "Nombre de usuario:", parent=ventana_seguridad)
        nueva_contraseña = simpledialog.askstring("Nueva Contraseña", "Ingrese la nueva contraseña:",
                                                  parent=ventana_seguridad)

        if servicio and usuario and nueva_contraseña:
            agregar_contraseña(servicio, usuario, nueva_contraseña)
            actualizar_lista()
        else:
            messagebox.showwarning("Campos Vacíos", "Todos los campos deben ser completados.", parent=ventana_seguridad)


    def generar_contraseña_segura():
        nueva_contrasena = generar_contrasena_segura()  # Generamos la contraseña aleatoria segura
        servicio = simpledialog.askstring("Nuevo Servicio", "Nombre del servicio:", parent=ventana_seguridad)
        usuario = simpledialog.askstring("Nuevo Usuario", "Nombre de usuario:", parent=ventana_seguridad)

        if servicio and usuario:

            messagebox.showinfo("Contraseña Generada", f"Contraseña generada: {nueva_contrasena}",
                                parent=ventana_seguridad)
            agregar_contraseña(servicio, usuario, nueva_contrasena)
            actualizar_lista()
        else:
            messagebox.showwarning("Campos Vacíos", "Todos los campos deben ser completados.", parent=ventana_seguridad)

    def exportar_contrasenas():
        archivo = filedialog.asksaveasfilename(
            title="Guardar archivo de contraseñas",
            defaultextension=".csv",
            filetypes=[("Archivos CSV", "*.csv"), ("Archivos de texto", "*.txt")]
        )
        if not archivo:
            return

        try:
            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()

            cursor.execute("SELECT sitio, usuario, password FROM contrasenas")
            contraseñas = cursor.fetchall()

            with open(archivo, "w") as f:
                for sitio, usuario, password in contraseñas:
                    f.write(f"{sitio},{usuario},{password}\n")

            conexion.close()
            messagebox.showinfo("Exportación Exitosa", "Se exportaron las contraseñas correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al exportar: {e}")

    def importar_contrasenas():

        archivo = filedialog.askopenfilename(
            title="Seleccionar archivo de contraseñas",
            filetypes=[("Archivos CSV", "*.csv"), ("Archivos de texto", "*.txt")]
        )
        if not archivo:
            return

        try:
            with open(archivo, "r") as f:
                contraseñas = [line.strip().split(",") for line in f.readlines()]

            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()

            for sitio, usuario, password in contraseñas:
                cursor.execute(
                    "INSERT INTO contrasenas (sitio, usuario, password) VALUES (?, ?, ?)",
                    (sitio, usuario, password)
                )

            conexion.commit()
            conexion.close()
            messagebox.showinfo("Importación Exitosa", "Se importaron las contraseñas correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Hubo un problema al importar: {e}")

    def gestor_contrasenas():
        subprocess.run(["python", "Gestor_contrasenas.py"])

    def notificaciones_seguridad():
        subprocess.run(["python", "notificaciones_seguridad.py"])

    def salir():
        ventana_seguridad.destroy()
        iniciar_aplicacion(nombre_usuario)


    frame_botones = tk.Frame(ventana_seguridad)
    frame_botones.pack(fill="x", padx=10, pady=10)
    tk.Button(frame_botones, text="Generar Contraseña", command=generar_contraseña, bg="lightblue").pack(side="left",
                                                                                                         padx=5)
    tk.Button(frame_botones, text="Generar Contraseña Aleatoria", command=generar_contraseña_segura,
              bg="lightgreen").pack(side="left", padx=5)

    btn_exportar = tk.Button(frame_botones, text="Exportar Contraseñas", command=exportar_contrasenas)
    btn_exportar.pack(pady=20)

    btn_importar = tk.Button(frame_botones, text="Importar Contraseñas", command=importar_contrasenas)
    btn_importar.pack(pady=20)

    btn_gestor = tk.Button(frame_botones, text="Gestionar Contraseñas", command=gestor_contrasenas)
    btn_gestor.pack(pady=20)

    btn_noti = tk.Button(frame_botones, text="Notificación de Seguridad", command=notificaciones_seguridad)
    btn_noti.pack(pady=20)

    btn_salir = tk.Button(frame_botones, text="Salir", command=salir)
    btn_salir.pack(pady=20)


    frame_lista = tk.Frame(ventana_seguridad)
    frame_lista.pack(fill="both", expand=True, padx=10, pady=10)


    actualizar_lista()

    ventana_seguridad.mainloop()