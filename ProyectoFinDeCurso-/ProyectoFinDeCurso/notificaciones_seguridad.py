import tkinter as tk
from tkinter import filedialog, messagebox
import threading
import time
import random


def verificar_contraseñas_comprometidas():
    while True:
        time.sleep(5)


        if random.choice([True, False]):
            messagebox.showwarning("¡Alerta de Seguridad!", "Una de tus contraseñas ha sido comprometida.")



def iniciar_verificacion():
    hilo = threading.Thread(target=verificar_contraseñas_comprometidas, daemon=True)
    hilo.start()


ventana = tk.Tk()
ventana.title("Notificaciones de Seguridad")

btn_iniciar = tk.Button(ventana, text="Iniciar Verificación de Seguridad", command=iniciar_verificacion)
btn_iniciar.pack(pady=20)

ventana.mainloop()
