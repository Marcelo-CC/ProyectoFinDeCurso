from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QMessageBox
import sqlite3
from src.logica.db import DB


DB.inicializar_db()


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(300, 450)


        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 300, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("E:/ProyectosCS/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos/Crear1.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")


        self.lineEdit_nombre = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_nombre.setGeometry(QtCore.QRect(90, 60, 113, 20))
        self.lineEdit_nombre.setObjectName("lineEdit_nombre")

        self.lineEdit_alias = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_alias.setGeometry(QtCore.QRect(90, 110, 113, 20))
        self.lineEdit_alias.setObjectName("lineEdit_alias")

        self.lineEdit_correo = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_correo.setGeometry(QtCore.QRect(90, 180, 113, 20))
        self.lineEdit_correo.setObjectName("lineEdit_correo")

        self.lineEdit_contrasena = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_contrasena.setGeometry(QtCore.QRect(90, 240, 113, 20))
        self.lineEdit_contrasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_contrasena.setObjectName("lineEdit_contrasena")

        self.lineEdit_confirmar_contrasena = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_confirmar_contrasena.setGeometry(QtCore.QRect(90, 310, 113, 20))
        self.lineEdit_confirmar_contrasena.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_confirmar_contrasena.setObjectName("lineEdit_confirmar_contrasena")


        self.label_nombre = QtWidgets.QLabel(parent=Dialog)
        self.label_nombre.setGeometry(QtCore.QRect(110, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_nombre.setFont(font)
        self.label_nombre.setObjectName("label_nombre")

        self.label_alias = QtWidgets.QLabel(parent=Dialog)
        self.label_alias.setGeometry(QtCore.QRect(120, 90, 47, 13))
        self.label_alias.setFont(font)
        self.label_alias.setObjectName("label_alias")

        self.label_correo = QtWidgets.QLabel(parent=Dialog)
        self.label_correo.setGeometry(QtCore.QRect(90, 150, 141, 20))
        self.label_correo.setFont(font)
        self.label_correo.setObjectName("label_correo")

        self.label_contrasena = QtWidgets.QLabel(parent=Dialog)
        self.label_contrasena.setGeometry(QtCore.QRect(90, 220, 81, 16))
        self.label_contrasena.setFont(font)
        self.label_contrasena.setObjectName("label_contrasena")

        self.label_confirmar_contrasena = QtWidgets.QLabel(parent=Dialog)
        self.label_confirmar_contrasena.setGeometry(QtCore.QRect(60, 280, 161, 20))
        self.label_confirmar_contrasena.setFont(font)
        self.label_confirmar_contrasena.setObjectName("label_confirmar_contrasena")


        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(90, 350, 91, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.registrar_usuario)  # Conectar al método de registro

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Registro de usuario"))
        self.label_nombre.setText(_translate("Dialog", "Nombre:"))
        self.label_alias.setText(_translate("Dialog", "Alias:"))
        self.label_correo.setText(_translate("Dialog", "Correo:"))
        self.label_contrasena.setText(_translate("Dialog", "Contraseña:"))
        self.label_confirmar_contrasena.setText(_translate("Dialog", "Confirmar contraseña:"))
        self.pushButton.setText(_translate("Dialog", "Registrar"))

    def registrar_usuario(self):

        nombre = self.lineEdit_nombre.text()
        alias = self.lineEdit_alias.text()
        correo = self.lineEdit_correo.text()
        contrasena = self.lineEdit_contrasena.text()
        confirmar_contrasena = self.lineEdit_confirmar_contrasena.text()


        if not nombre or not alias or not correo or not contrasena:
            QMessageBox.critical(None, "Error", "Todos los campos son obligatorios.")
            return
        if contrasena != confirmar_contrasena:
            QMessageBox.critical(None, "Error", "Las contraseñas no coinciden.")
            return

        try:

            DB.insertar_usuario(nombre, alias, correo, contrasena)
            QMessageBox.information(None, "Éxito", "Usuario registrado correctamente.")


            conexion = sqlite3.connect("usuarios.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT id FROM usuarios WHERE correo = ?", (correo,))
            id_usuario = cursor.fetchone()[0]
            conexion.close()


            self.abrir_preguntas_seguridad(id_usuario)

        except ValueError as e:
            QMessageBox.critical(None, "Error", str(e))

    def abrir_preguntas_seguridad(self, id_usuario):
        self.ventana_preguntas = QtWidgets.QDialog()
        self.ui_preguntas = Ui_PreguntasSeguridad()
        self.ui_preguntas.setupUi(self.ventana_preguntas, id_usuario)
        self.ventana_preguntas.exec()


# Ventana para preguntas de seguridad
class Ui_PreguntasSeguridad(object):
    def setupUi(self, Dialog, id_usuario):
        self.id_usuario = id_usuario
        Dialog.setObjectName("PreguntasSeguridad")
        Dialog.resize(400, 300)

        # Preguntas
        self.label_pregunta1 = QtWidgets.QLabel(parent=Dialog)
        self.label_pregunta1.setGeometry(QtCore.QRect(50, 50, 300, 20))
        self.label_pregunta1.setText("Pregunta 1: ¿Cuál es tu color favorito?")

        self.lineEdit_respuesta1 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_respuesta1.setGeometry(QtCore.QRect(50, 80, 300, 20))

        self.label_pregunta2 = QtWidgets.QLabel(parent=Dialog)
        self.label_pregunta2.setGeometry(QtCore.QRect(50, 120, 300, 20))
        self.label_pregunta2.setText("Pregunta 2: ¿Cuál es el nombre de tu primera mascota?")

        self.lineEdit_respuesta2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_respuesta2.setGeometry(QtCore.QRect(50, 150, 300, 20))

        # Botón
        self.pushButton_guardar = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_guardar.setGeometry(QtCore.QRect(150, 200, 100, 30))
        self.pushButton_guardar.setText("Guardar")
        self.pushButton_guardar.clicked.connect(self.guardar_preguntas)

    def guardar_preguntas(self):
        respuesta1 = self.lineEdit_respuesta1.text()
        respuesta2 = self.lineEdit_respuesta2.text()

        if not respuesta1 or not respuesta2:
            QMessageBox.critical(None, "Error", "Todas las respuestas son obligatorias.")
            return

        preguntas_respuestas = [
            ("¿Cuál es tu color favorito?", respuesta1),
            ("¿Cuál es el nombre de tu primera mascota?", respuesta2),
        ]

        DB.agregar_preguntas_seguridad(self.id_usuario, preguntas_respuestas)
        QMessageBox.information(None, "Éxito", "Preguntas de seguridad guardadas.")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())