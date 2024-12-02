from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import subprocess
import ventana_seguridad
from Crear_Categorias_Contraseña import CategoriaPasswordsGUI
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.Dialog = Dialog  # Mantener referencia


        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 300))
        self.label.setPixmap(QtGui.QPixmap("E:/ProyectosCS/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos/Aplicacion.jpg"))
        self.label.setScaledContents(True)


        self.label_user_icon = QtWidgets.QLabel(Dialog)
        self.label_user_icon.setGeometry(QtCore.QRect(20, 20, 60, 60))
        self.label_user_icon.setPixmap(QtGui.QPixmap("E:/ProyectosCS/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos/Usuario.jpg"))
        self.label_user_icon.setScaledContents(True)


        self.label_user_name = QtWidgets.QLabel(Dialog)
        self.label_user_name.setGeometry(QtCore.QRect(100, 30, 200, 30))
        self.label_user_name.setStyleSheet("font-size: 16px; font-weight: bold; color: white;")


        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 80, 100, 30))
        self.pushButton.setText("Cerrar Sesión")
        self.pushButton.clicked.connect(self.cerrar_sesion)

        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 120, 120, 30))
        self.pushButton_2.setText("Información")

        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 170, 120, 30))
        self.pushButton_3.setText("Seguridad")
        self.pushButton_3.clicked.connect(self.abrir_seguridad)

        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 120, 120, 30))
        self.pushButton_4.setText("Datos y Privacidad")

        self.pushButton_5 = QtWidgets.QPushButton(Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(220, 170, 120, 30))
        self.pushButton_5.setText("Pagos y Suscripciones")

        self.pushButton_6 = QtWidgets.QPushButton(Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(100, 230, 200, 30))
        self.pushButton_6.setText("Crear Categorías de Contraseña")
        self.pushButton_6.clicked.connect(self.iniciar_crear_categorias)

    def cerrar_sesion(self):

        QtWidgets.QMessageBox.information(self.Dialog, "Cierre de Sesión", "Has cerrado sesión exitosamente.")
        self.Dialog.close()
        ruta = os.path.join(os.path.dirname(__file__), "main_login.py")
        subprocess.run([sys.executable, ruta])  # Llama al script del login

    def abrir_seguridad(self):

        ventana_seguridad.iniciar_ventana_seguridad(self.nombre_usuario)

    def iniciar_crear_categorias(self):

        id_usuario = self.obtener_id_usuario(self.nombre_usuario)
        if id_usuario:
            app = CategoriaPasswordsGUI(id_usuario=id_usuario)
            app.run()
        else:
            QtWidgets.QMessageBox.critical(self.Dialog, "Error", "Usuario no encontrado.")

    @staticmethod
    def obtener_id_usuario(nombre_usuario):

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE alias = ?", (nombre_usuario,))
        usuario = cursor.fetchone()
        conexion.close()
        return usuario[0] if usuario else None


def iniciar_aplicacion(nombre_usuario):

    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.nombre_usuario = nombre_usuario
    ui.setupUi(Dialog)
    ui.label_user_name.setText(f"Bienvenido, {nombre_usuario}")  # Mostrar el nombre del usuario
    Dialog.exec()



if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        nombre_usuario = sys.argv[1]
        iniciar_aplicacion(nombre_usuario)
    else:
        print("Error: No se proporcionó el nombre del usuario.")
