from PyQt5 import QtCore, QtGui, QtWidgets
from sixth import Ui_Form5
class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 125)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(165, 10, 70, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(100, 40, 40, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(100, 70, 40, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(140, 40, 160, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 70, 160, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(165, 100, 50, 20))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.reg)
    def reg(self):
        if (self.lineEdit.text()=="admin" and self.lineEdit_2.text()=="123"):
            self.Form5 = QtWidgets.QWidget()
            self.ui = Ui_Form5()
            self.ui.setupUi(self.Form5)
            self.Form5.setStyleSheet("#Form{background-color:white}")
            self.Form5.show()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Авторизация"))
        self.label.setText(_translate("Form", "Авторизация"))
        self.label_2.setText(_translate("Form", "Логин"))
        self.label_3.setText(_translate("Form", "Пароль"))
        self.pushButton.setText(_translate("Form", "Ok"))