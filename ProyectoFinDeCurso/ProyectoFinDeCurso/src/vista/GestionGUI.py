# Form implementation generated from reading ui file 'Gestion.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(527, 300)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 621, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../recursos/Gestion.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.pushButton_6 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_6.setGeometry(QtCore.QRect(390, 180, 131, 31))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(160, 40, 161, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_7 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_7.setGeometry(QtCore.QRect(390, 220, 111, 31))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(390, 140, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 60, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(390, 100, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(30, 40, 111, 31))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Gestion de contraseñas"))
        self.pushButton_6.setText(_translate("Dialog", "Notificación de Seguridad"))
        self.pushButton_2.setText(_translate("Dialog", "Generar contraseña Aleatoria "))
        self.pushButton_7.setText(_translate("Dialog", "Salir"))
        self.pushButton_5.setText(_translate("Dialog", "Gestionar contraseñas"))
        self.pushButton_3.setText(_translate("Dialog", "Exportar Contraseñas"))
        self.pushButton_4.setText(_translate("Dialog", "Importar contraseñas"))
        self.pushButton.setText(_translate("Dialog", "Generar Contraseña"))
