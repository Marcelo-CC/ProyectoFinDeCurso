# Form implementation generated from reading ui file 'Aplicacion.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(398, 272)
        self.label = QtWidgets.QLabel(parent=Dialog)
        self.label.setGeometry(QtCore.QRect(0, 0, 401, 301))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../recursos/Aplicacion.jpg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(parent=Dialog)
        self.label_2.setGeometry(QtCore.QRect(110, 30, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton.setGeometry(QtCore.QRect(100, 60, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 140, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 200, 91, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(210, 140, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_5.setGeometry(QtCore.QRect(210, 200, 121, 31))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label_3 = QtWidgets.QLabel(parent=Dialog)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 71, 61))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../recursos/Usuario.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Aplicacion"))
        self.label_2.setText(_translate("Dialog", "TextLabel"))
        self.pushButton.setText(_translate("Dialog", "Cerrar Sesión"))
        self.pushButton_2.setText(_translate("Dialog", "Información"))
        self.pushButton_3.setText(_translate("Dialog", "Seguridad"))
        self.pushButton_4.setText(_translate("Dialog", "Datos y Privacidad"))
        self.pushButton_5.setText(_translate("Dialog", "Pagos y Suscripciones"))
