from PyQt6 import QtCore, QtGui, QtWidgets
import subprocess
import os

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(330, 402)

        # Fondo
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 331, 401))
        self.label.setPixmap(QtGui.QPixmap("E:/ProyectosCS/ProyectoFinDeCurso-/ProyectoFinDeCurso/src/recursos/Login.jpg"))  # Cambiar a la ruta real
        self.label.setScaledContents(True)
        self.label.setObjectName("label")

        # Etiqueta de bienvenida
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(115, 70, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")

        # Botón Crear Cuenta
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(115, 160, 101, 31))
        self.pushButton.setObjectName("pushButton")

        # Botón Iniciar Sesión
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(115, 230, 101, 31))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.abrir_crear_cuenta)
        self.pushButton_2.clicked.connect(self.abrir_iniciar_sesion)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Bienvenida"))
        self.label_2.setText(_translate("Dialog", "BIENVENIDO"))
        self.pushButton.setText(_translate("Dialog", "CREAR CUENTA"))
        self.pushButton_2.setText(_translate("Dialog", "INICIAR SESIÓN"))

    def abrir_crear_cuenta(self):
        """Abre el script de crear cuenta."""
        ruta = os.path.join(os.path.dirname(__file__), "main_registro.py")
        subprocess.run([sys.executable, ruta])

    def abrir_iniciar_sesion(self):
        """Abre el script de iniciar sesión."""
        ruta = os.path.join(os.path.dirname(__file__), "main_login.py")
        subprocess.run([sys.executable, ruta])


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())