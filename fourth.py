import pymongo
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["museum"]
collection = current_db["Weapon"]
from PyQt5 import QtCore, QtGui, QtWidgets
ammountwe = 0
numberwe = 0
class Ui_Form3(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 700)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(650, 70, 71, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(730, 70, 171, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("1A")
        self.comboBox.addItem("1B")
        self.comboBox.addItem("1C")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 630, 660))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Michail/Downloads/swords (1).jpg"))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(650, 100, 71, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(650, 120, 71, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(650, 140, 71, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(650, 160, 71, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(650, 180, 71, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(720, 100, 181, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(720, 120, 181, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(720, 140, 181, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(720, 160, 181, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(720, 180, 461, 490))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(1050, 140, 131, 23))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 140, 131, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.Checator()
        self.comboBox.currentTextChanged.connect(self.Checator)
        self.pushButton.clicked.connect(self.next)
        self.pushButton_2.clicked.connect(self.previous)
    def Checator(self):
        global numberwe
        global ammountwe
        ammountwe = 0
        numberwe = 0
        newweapon = collection.find({'location': self.comboBox.currentText()})[0]
        ammountwe = collection.count_documents({"location": {"$eq": self.comboBox.currentText()}})
        self.lineEdit.setText(newweapon['name'])
        self.lineEdit_2.setText(newweapon['type'])
        self.lineEdit_3.setText(newweapon['attack type'])
        self.lineEdit_4.setText(str(newweapon['year']))
        self.textEdit.setPlainText(newweapon['description'])
        if self.comboBox.currentText() == "1A":
            self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Michail/PycharmProjects/pythonProject2/swords.jpg"))
        elif self.comboBox.currentText() == "1B":
            self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Michail/PycharmProjects/pythonProject2/mases.png"))
        elif self.comboBox.currentText() == "1C":
            self.label_2.setPixmap(QtGui.QPixmap("C:/Users/Michail/PycharmProjects/pythonProject2/polearms.jpeg"))
    def next(self):
        global numberwe
        global ammountwe
        numberwe += 1
        if numberwe >= ammountwe:
            numberwe = 0
        newweapon = collection.find({'location': self.comboBox.currentText()})[numberwe]
        self.lineEdit.setText(newweapon['name'])
        self.lineEdit_2.setText(newweapon['type'])
        self.lineEdit_3.setText(newweapon['attack type'])
        self.lineEdit_4.setText(str(newweapon['year']))
        self.textEdit.setPlainText(newweapon['description'])
    def previous(self):
        global numberwe
        global ammountwe
        numberwe -= 1
        if numberwe < 0:
            numberwe = ammountwe - 1
        newweapon = collection.find({'location': self.comboBox.currentText()})[numberwe]
        self.lineEdit.setText(newweapon['name'])
        self.lineEdit_2.setText(newweapon['type'])
        self.lineEdit_3.setText(newweapon['attack type'])
        self.lineEdit_4.setText(str(newweapon['year']))
        self.textEdit.setPlainText(newweapon['description'])
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Экспонаты"))
        self.label.setText(_translate("Form", "Выберите зал"))
        self.label_3.setText(_translate("Form", "Название"))
        self.label_4.setText(_translate("Form", "Тип"))
        self.label_5.setText(_translate("Form", "Тип атаки"))
        self.label_6.setText(_translate("Form", "Год"))
        self.label_7.setText(_translate("Form", "Описание"))
        self.pushButton.setText(_translate("Form", "Следующий экземпляр"))
        self.pushButton_2.setText(_translate("Form", "Предыдущий экземпляр"))