from PyQt6 import QtCore, QtGui, QtWidgets
from src.logica.iniciar_sesion import Login
import sys
import subprocess


class Ui_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(329, 353)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 421))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("D:/ProyectoFinDeCurso--20241202T190310Z-001/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(140, 40, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(110, 70, 113, 20))
        self.lineEdit.setObjectName("lineEdit")  # Alias
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(110, 130, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Algerian")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 170, 113, 20))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)  # Contraseña oculta
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(110, 230, 111, 31))
        self.pushButton.setObjectName("pushButton")  # Botón iniciar sesión
        self.pushButton.clicked.connect(self.iniciar_sesion)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 290, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")  # Botón olvidar contraseña
        self.pushButton_2.clicked.connect(self.abrir_recuperar_contrasena)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Inicio de sesión"))
        self.label_2.setText(_translate("Dialog", "ALIAS:"))
        self.label_3.setText(_translate("Dialog", "CONTRASEÑA:"))
        self.pushButton.setText(_translate("Dialog", "INICIAR SESIÓN:"))
        self.pushButton_2.setText(_translate("Dialog", "¿OLVIDASTE TU CONTRASEÑA?"))

    def iniciar_sesion(self):
        alias = self.lineEdit.text().strip()
        contrasena = self.lineEdit_2.text().strip()

        if not alias or not contrasena:
            QtWidgets.QMessageBox.critical(self, "Error", "Por favor, completa todos los campos.")
            return

        if Login.validar_credenciales(alias, contrasena):
            QtWidgets.QMessageBox.information(self, "Éxito", f"Bienvenido, {alias}!")
            self.close()
            subprocess.run([sys.executable, "main_aplicacion.py", alias])
        else:
            QtWidgets.QMessageBox.critical(self, "Error", "Credenciales incorrectas.")

    def abrir_recuperar_contrasena(self):
        self.close()
        subprocess.run([sys.executable, "recuperar_contrasena.py"])


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Dialog = Ui_Dialog()
    Dialog.show()
    sys.exit(app.exec())
