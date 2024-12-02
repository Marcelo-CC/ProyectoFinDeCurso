import tkinter as tk
from tkinter import simpledialog, messagebox
from tkinter import ttk
from src.logica.db import DB


class CategoriaPasswordsGUI:
    def __init__(self, id_usuario):

        self.id_usuario = id_usuario
        self.root = tk.Tk()
        self.root.title("Gestión de Categorías y Contraseñas")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        # Establecer un estilo para los widgets
        self.estilo = ttk.Style()
        self.estilo.configure("TButton", font=("Arial", 10, "bold"), padding=6, relief="flat", background="#4CAF50")
        self.estilo.configure("TListbox", font=("Arial", 12), height=6, relief="solid", borderwidth=2)

        self.create_widgets()
        self.cargar_categorias()

    def create_widgets(self):

        frame = ttk.Frame(self.root, padding="10")
        frame.pack(fill=tk.BOTH, expand=True)


        self.listbox_frame = ttk.Frame(frame)
        self.listbox_frame.pack(fill=tk.BOTH, expand=True)

        self.listbox_categorias = tk.Listbox(self.listbox_frame, height=10, width=40, font=("Arial", 12), bd=2,
                                             relief="solid")
        self.listbox_categorias.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)


        scrollbar = ttk.Scrollbar(self.listbox_frame, orient="vertical", command=self.listbox_categorias.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox_categorias.config(yscrollcommand=scrollbar.set)


        button_frame = ttk.Frame(frame, padding="10")
        button_frame.pack(pady=10)

        self.btn_agregar_categoria = self.create_button(button_frame, "Agregar Categoría", self.agregar_categoria)
        self.btn_agregar_categoria.grid(row=0, column=0, padx=5)

        self.btn_editar_categoria = self.create_button(button_frame, "Editar Categoría", self.editar_categoria)
        self.btn_editar_categoria.grid(row=0, column=1, padx=5)

        self.btn_eliminar_categoria = self.create_button(button_frame, "Eliminar Categoría", self.eliminar_categoria)
        self.btn_eliminar_categoria.grid(row=0, column=2, padx=5)

        self.btn_agregar_contraseña = self.create_button(button_frame, "Agregar Contraseña", self.agregar_contraseña)
        self.btn_agregar_contraseña.grid(row=1, column=0, padx=5)

        self.btn_ver_contraseñas = self.create_button(button_frame, "Ver Contraseñas", self.ver_contraseñas)
        self.btn_ver_contraseñas.grid(row=1, column=1, padx=5)

    def create_button(self, parent, text, command):

        button = ttk.Button(parent, text=text, command=command, style="TButton")
        return button

    def cargar_categorias(self):

        try:
            self.listbox_categorias.delete(0, tk.END)  # Limpiar la lista antes de cargar
            categorias = DB.obtener_categorias(self.id_usuario)

            if categorias:
                for categoria in categorias:
                    self.listbox_categorias.insert(tk.END, categoria)
            else:
                messagebox.showinfo("Sin categorías", "No tienes categorías asociadas.")
        except Exception as e:
            messagebox.showerror("Error", f"Ocurrió un error al cargar las categorías: {e}")

    def agregar_categoria(self):

        nueva_categoria = simpledialog.askstring("Nueva Categoría", "Ingresa el nombre de la categoría:")

        if nueva_categoria:
            nueva_categoria = nueva_categoria.strip()


            if not nueva_categoria:
                messagebox.showwarning("Entrada inválida", "El nombre de la categoría no puede estar vacío.")
                return

            if self.validar_categoria_existente(nueva_categoria):
                messagebox.showwarning("Categoría existente", "La categoría ya existe.")
                return

            try:
                DB.insertar_categoria(self.id_usuario, nueva_categoria)
                self.cargar_categorias()  # Recargar las categorías
                messagebox.showinfo("Categoría agregada",
                                    f"La categoría '{nueva_categoria}' fue agregada exitosamente.")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error al agregar la categoría: {e}")
        else:
            messagebox.showwarning("Entrada inválida", "Debes ingresar un nombre para la categoría.")

    def eliminar_categoria(self):
        """
        Eliminar la categoría seleccionada de la base de datos.
        """
        seleccion = self.listbox_categorias.curselection()
        if seleccion:
            categoria = self.listbox_categorias.get(seleccion[0])
            confirmacion = messagebox.askyesno("Confirmar eliminación",
                                               f"¿Estás seguro de que deseas eliminar la categoría '{categoria}'?")

            if confirmacion:
                try:
                    DB.eliminar_categoria(self.id_usuario, categoria)
                    self.cargar_categorias()  # Recargar las categorías
                    messagebox.showinfo("Categoría eliminada", f"La categoría '{categoria}' ha sido eliminada.")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al eliminar la categoría: {e}")
        else:
            messagebox.showwarning("Selección inválida", "Debes seleccionar una categoría para eliminar.")

    def editar_categoria(self):
        """
        Editar la categoría seleccionada.
        """
        seleccion = self.listbox_categorias.curselection()
        if seleccion:
            categoria_actual = self.listbox_categorias.get(seleccion[0])
            nuevo_nombre = simpledialog.askstring("Editar Categoría",
                                                  f"Ingresa el nuevo nombre para la categoría '{categoria_actual}':")

            if nuevo_nombre:
                nuevo_nombre = nuevo_nombre.strip()

                # Validar que no esté vacía ni duplicada
                if not nuevo_nombre:
                    messagebox.showwarning("Entrada inválida", "El nombre de la categoría no puede estar vacío.")
                    return

                if self.validar_categoria_existente(nuevo_nombre):
                    messagebox.showwarning("Categoría existente", "La categoría ya existe.")
                    return

                try:
                    DB.editar_categoria(self.id_usuario, categoria_actual, nuevo_nombre)
                    self.cargar_categorias()  # Recargar las categorías
                    messagebox.showinfo("Categoría editada", f"La categoría ha sido renombrada a '{nuevo_nombre}'.")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al editar la categoría: {e}")
        else:
            messagebox.showwarning("Selección inválida", "Debes seleccionar una categoría para editar.")

    def agregar_contraseña(self):

        seleccion = self.listbox_categorias.curselection()
        if seleccion:
            categoria = self.listbox_categorias.get(seleccion[0])
            contraseña = simpledialog.askstring("Nueva Contraseña",
                                                f"Ingresa la contraseña para la categoría '{categoria}':")

            if contraseña:
                try:
                    DB.insertar_contraseña(self.id_usuario, categoria, contraseña)
                    messagebox.showinfo("Contraseña agregada", "La contraseña fue agregada exitosamente.")
                except Exception as e:
                    messagebox.showerror("Error", f"Ocurrió un error al agregar la contraseña: {e}")
        else:
            messagebox.showwarning("Selección inválida", "Debes seleccionar una categoría para agregar la contraseña.")

    def ver_contraseñas(self):

        seleccion = self.listbox_categorias.curselection()
        if seleccion:
            categoria = self.listbox_categorias.get(seleccion[0])
            contraseñas = DB.obtener_contraseñas(self.id_usuario, categoria)

            if contraseñas:
                contraseñas_texto = "\n".join(contraseñas)
                messagebox.showinfo(f"Contraseñas de '{categoria}'", contraseñas_texto)
            else:
                messagebox.showinfo("Sin contraseñas", f"No hay contraseñas asociadas a la categoría '{categoria}'.")
        else:
            messagebox.showwarning("Selección inválida", "Debes seleccionar una categoría para ver las contraseñas.")

    def validar_categoria_existente(self, categoria):

        categorias = DB.obtener_categorias(self.id_usuario)
        return categoria in categorias

    def run(self):

        self.root.mainloop()



if __name__ == "__main__":
    app = CategoriaPasswordsGUI(id_usuario=1)
    app.run()
