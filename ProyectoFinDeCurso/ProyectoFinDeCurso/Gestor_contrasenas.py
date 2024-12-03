import tkinter as tk
from tkinter import messagebox
import re
import random
import string
import os


def evaluar_contrasena():
    contrasena = entry_contrasena.get()
    sugerencias = []

    if len(contrasena) < 8:
        sugerencias.append("La contraseña debe tener al menos 8 caracteres.")
    if not re.search(r"[A-Z]", contrasena):
        sugerencias.append("Agrega al menos una letra mayúscula.")
    if not re.search(r"[a-z]", contrasena):
        sugerencias.append("Agrega al menos una letra minúscula.")
    if not re.search(r"[0-9]", contrasena):
        sugerencias.append("Agrega al menos un número.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena):
        sugerencias.append("Agrega al menos un carácter especial (!@#$%^&*).")

    if sugerencias:
        messagebox.showwarning("Contraseña débil", "\n".join(sugerencias))
    else:
        messagebox.showinfo("Contraseña segura", "¡La contraseña es segura!")


def generar_contrasena_segura():
    longitud = 12
    caracteres = string.ascii_letters + string.digits + "!@#$%^&*()"
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))

    while (not re.search(r"[A-Z]", contrasena) or
           not re.search(r"[a-z]", contrasena) or
           not re.search(r"[0-9]", contrasena) or
           not re.search(r"[!@#$%^&*(),.?\":{}|<>]", contrasena)):
        contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena


def autocompletar_contrasena():
    contrasena_segura = generar_contrasena_segura()  # Generar contraseña segura
    formulario_password.delete(0, tk.END)
    formulario_password.insert(0, contrasena_segura)

def salir():
    ventana.destroy()  # Cierra la ventana actual
    os.system("python ventana_seguridad.py")


ventana = tk.Tk()
ventana.title("Gestión de Contraseñas")
ventana.geometry("300x300")


tk.Label(ventana, text="Evaluar Seguridad de Contraseña").pack(pady=10)
entry_contrasena = tk.Entry(ventana, show="*")
entry_contrasena.pack(pady=5)
tk.Button(ventana, text="Evaluar", command=evaluar_contrasena).pack(pady=5)


tk.Label(ventana, text="Autocompletar Contraseña").pack(pady=10)
formulario_password = tk.Entry(ventana)
formulario_password.pack(pady=5)
tk.Button(ventana, text="Autocompletar", command=autocompletar_contrasena).pack(pady=5)

tk.Button(ventana, text="Salir", command=salir, bg="red", fg="white").pack(pady=20)
ventana.mainloop()
