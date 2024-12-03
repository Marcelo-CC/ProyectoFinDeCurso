from PyQt6 import QtCore, QtGui, QtWidgets
import sqlite3
import hashlib


def hash_password(password):

    return hashlib.sha256(password.encode()).hexdigest()


def enviar_correo_restauracion(email):

    print(f"Enlace de restauración enviado a {email}. Enlace: http://www.cambiarcontrasena.com.pe")
    return True


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 600)
        self.Dialog = Dialog


        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 400, 600))
        self.label.setPixmap(QtGui.QPixmap("E:/ProyectosCS/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos/Recuperar.jpg"))
        self.label.setScaledContents(True)


        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 360, 40))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setText("INTRODUCE TU CORREO ELECTRÓNICO PARA BUSCAR TU CUENTA")


        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 80, 320, 30))
        self.lineEdit.setPlaceholderText("Correo electrónico")


        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(250, 130, 100, 30))
        self.pushButton_2.setText("BUSCAR")
        self.pushButton_2.clicked.connect(self.buscar_usuario)


        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 100, 30))
        self.pushButton.setText("CANCELAR")
        self.pushButton.clicked.connect(self.cancelar)


        self.label_6 = QtWidgets.QLabel(parent=Dialog)
        self.label_6.setGeometry(QtCore.QRect(40, 180, 100, 20))
        self.label_6.setText("Nombre:")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(40, 200, 320, 30))
        self.lineEdit_2.setPlaceholderText("Nombre")
        self.lineEdit_2.setEnabled(False)


        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 100, 20))
        self.label_3.setText("Alias:")
        self.lineEdit_3 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_3.setGeometry(QtCore.QRect(40, 270, 320, 30))
        self.lineEdit_3.setPlaceholderText("Alias")
        self.lineEdit_3.setEnabled(False)


        self.label_4 = QtWidgets.QLabel(parent=Dialog)
        self.label_4.setGeometry(QtCore.QRect(40, 320, 120, 20))
        self.label_4.setText("Contraseña:")
        self.lineEdit_5 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 340, 320, 30))
        self.lineEdit_5.setPlaceholderText("Nueva contraseña")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_5.setEnabled(False)


        self.label_5 = QtWidgets.QLabel(parent=Dialog)
        self.label_5.setGeometry(QtCore.QRect(40, 390, 180, 20))
        self.label_5.setText("Confirmar contraseña:")
        self.lineEdit_6 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 410, 320, 30))
        self.lineEdit_6.setPlaceholderText("Confirmar contraseña")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEdit_6.setEnabled(False)


        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 470, 100, 40))
        self.pushButton_3.setText("Registrar")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.registrar_contrasena)

    def cancelar(self):

        self.Dialog.close()

    def buscar_usuario(self):

        email = self.lineEdit.text().strip()

        if not email:
            QtWidgets.QMessageBox.critical(self.Dialog, "Error", "Por favor, introduce un correo electrónico.")
            return

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        try:
            cursor.execute("SELECT nombre, alias FROM usuarios WHERE correo = ?", (email,))
            usuario = cursor.fetchone()

            if usuario:
                nombre_usuario, alias_usuario = usuario
                self.lineEdit_2.setText(nombre_usuario)
                self.lineEdit_3.setText(alias_usuario)
                self.lineEdit_5.setEnabled(True)
                self.lineEdit_6.setEnabled(True)
                self.pushButton_3.setEnabled(True)
                enviar_correo_restauracion(email)
                QtWidgets.QMessageBox.information(
                    self.Dialog,
                    "Correo Enviado",
                    f"Se envió un enlace al correo electrónico {email}. Revisa tu bandeja.",
                )
            else:
                QtWidgets.QMessageBox.critical(self.Dialog, "Error", "El correo ingresado no está registrado.")
        finally:
            conexion.close()

    def registrar_contrasena(self):
        """Registra la nueva contraseña."""
        nueva_contrasena = self.lineEdit_5.text()
        confirmar_contrasena = self.lineEdit_6.text()

        if nueva_contrasena != confirmar_contrasena:
            QtWidgets.QMessageBox.critical(self.Dialog, "Error", "Las contraseñas no coinciden.")
            return

        email = self.lineEdit.text().strip()
        contrasena_hashed = hash_password(nueva_contrasena)

        conexion = sqlite3.connect("usuarios.db")
        cursor = conexion.cursor()

        try:
            cursor.execute("UPDATE usuarios SET contrasena = ? WHERE correo = ?", (contrasena_hashed, email))
            conexion.commit()
            QtWidgets.QMessageBox.information(self.Dialog, "Éxito", "La contraseña ha sido actualizada correctamente.")
            self.Dialog.close()
        finally:
            conexion.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
