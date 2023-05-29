import pymongo
import datetime
from fpdf import FPDF
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["museum"]
collection = current_db["Client"]
collection2 = current_db["Excursion"]
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 280)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(340, 250, 100, 30))
        self.pushButton.setObjectName("pushButton")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(392, 230, 36, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(430, 230, 35, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(470, 230, 36, 17))
        self.checkBox_3.setObjectName("checkBox_3")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(392, 178, 133, 20))
        self.comboBox.setObjectName("comboBox")
        T = datetime.date.today()
        T = datetime.datetime(T.year, T.month, T.day, 12)
        for i in range(5):
            self.comboBox.addItem(str(T))
            if (int(T.day) == 31):
                T = datetime.datetime(T.year, T.month + 1, 1, T.hour)
            else:
                T = datetime.datetime(T.year, T.month, T.day + 1, T.hour)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(392, 155, 70, 17))
        self.radioButton.setObjectName("radioButton")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(392, 51, 133, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(392, 77, 133, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(392, 103, 133, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(392, 129, 133, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(392, 204, 133, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 0, 600, 30))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(281, 51, 19, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(281, 77, 44, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(281, 103, 44, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(281, 129, 105, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(281, 178, 80, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(281, 155, 72, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(0, 30, 250, 200))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("C:/Users/Michail/PycharmProjects/pythonProject2/ticket.jpg"))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(550, 30, 250, 200))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("C:/Users/Michail/PycharmProjects/pythonProject2/ticket.jpg"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(281, 204, 73, 16))
        self.label_10.setObjectName("label_11")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(281, 230, 69, 16))
        self.label_11.setObjectName("label_12")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.reg)
        self.radioButton.clicked.connect(self.check)
    def reg(self):
        errno = QMessageBox()
        errno.setWindowTitle("Ошибка")
        errno.setText("Несоответствие форматов.")
        errno.setInformativeText("Экскурсия не может длится более 3 часов и на ней не могут присутствовать более 100 человек.")
        errno.setStandardButtons(QMessageBox.Cancel)
        if int(self.lineEdit_5.text()) > 3 or int(self.lineEdit_4.text()) > 100:
            btn = errno.exec_()
            if btn == QMessageBox.Cancel:
                return
        ammountcl = collection.count_documents({"client number": {"$gt": 0}}) + 1
        ammountex = collection2.count_documents({"number": {"$gt": 0}}) + 1
        H = [" ", " ", " "]
        if self.checkBox.isChecked():
            H[0] = self.checkBox.text()
        if self.checkBox_2.isChecked():
            H[1] = self.checkBox_2.text()
        if self.checkBox_3.isChecked():
            H[2] = self.checkBox_3.text()
        for i in range(2,-1,-1):
            if H[i] == " ":
                H.pop(i)
        if self.radioButton.isChecked():
            price = "19.99"
            type = "registered"
            if (list(collection2.find({'date': self.comboBox.currentText()}))):
                warn = QMessageBox()
                warn.setWindowTitle("Предупреждение")
                warn.setText("На это время уже  запланированна экскурсия.")
                warn.setInformativeText("Если хотите присоеденится нажмите 'Ок'.")
                warn.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                btn = warn.exec_()
                if btn == QMessageBox.Cancel:
                    return
                if btn == QMessageBox.Ok:
                    warn.hide()
                ammountex -= 1
                for Excursion in collection2.find({'date': self.comboBox.currentText()}):
                    if int(self.lineEdit_4.text()) + int(Excursion["clients ammount"]) > 100:
                        btn = errno.exec_()
                        if btn == QMessageBox.Cancel:
                            return
                    A = int(Excursion["clients ammount"]) + int(self.lineEdit_4.text())
                    for i in Excursion["halls"]:
                        H.append(i)
                    H = list(set(H))
                    collection2.update_many({'date': self.comboBox.currentText()}, {'$set': {"clients ammount": A, "halls": H}, '$push': {"client numbers": ammountcl}})
                    if int(self.lineEdit_5.text()) > Excursion["duration"]:
                        collection2.update_many({'date': self.comboBox.currentText()}, {'$set': {"duration": self.lineEdit_5.text()}})
            else:
                newexcursion = {
                    "number": ammountex,
                    "type": "registered",
                    "duration": int(self.lineEdit_5.text()),
                    "guide service number": 6,
                    "halls": H,
                    "price per person": 19.99,
                    "clients ammount": int(self.lineEdit_4.text()),
                    "date": self.comboBox.currentText(),
                    "client numbers": [ammountcl]
                }
                collection2.insert_one(newexcursion)
        else:
            price = "9.99"
            type = "planned"
            if (list(collection2.find({'date': self.comboBox.currentText()}))):
                warn = QMessageBox()
                warn.setWindowTitle("Предупреждение")
                warn.setText("На это время уже  запланированна экскурсия.")
                warn.setInformativeText("Если хотите присоеденится нажмите 'Ок'.")
                warn.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
                btn = warn.exec_()
                if btn == QMessageBox.Cancel:
                    return
                if btn == QMessageBox.Ok:
                    warn.hide()
                ammountex -= 1
                for Excursion in collection2.find({'date': self.comboBox.currentText()}):
                    if int(self.lineEdit_4.text()) + int(Excursion["clients ammount"]) > 100:
                        btn = errno.exec_()
                        if btn == QMessageBox.Cancel:
                            return
                    A = int(Excursion["clients ammount"]) + int(self.lineEdit_4.text())
                    for i in Excursion["halls"]:
                        H.append(i)
                    H = list(set(H))
                    collection2.update_many({'date': self.comboBox.currentText()}, {'$set': {"clients ammount": A, "halls": H}, '$push': {"client numbers": ammountcl}})
                    if int(self.lineEdit_5.text()) > Excursion["duration"]:
                        collection2.update_many({'date': self.comboBox.currentText()}, {'$set': {"duration": self.lineEdit_5.text()}})
            else:
                newexcursion = {
                    "number": ammountex,
                    "type": "planned",
                    "duration": int(self.lineEdit_5.text()),
                    "guide service number": 2,
                    "halls": H,
                    "price per person": 9.99,
                    "clients ammount": int(self.lineEdit_4.text()),
                    "date": self.comboBox.currentText(),
                    "client numbers": [ammountcl]
                }
                collection2.insert_one(newexcursion)
        newclient = {
            "client number": ammountcl,
            "first name": self.lineEdit.text(),
            "second name": self.lineEdit_2.text(),
            "phone number": int(self.lineEdit_3.text()),
            "ammount": int(self.lineEdit_4.text()),
            "date of visit": self.comboBox.currentText(),
            "excursion number": ammountex
        }
        collection.insert_one(newclient)
        pdf = FPDF("P", "mm", "A4")
        pdf.add_page()
        pdf.add_font("TimesNR", "", "timesnrcyrmt.ttf", uni=True)
        pdf.set_font("TimesNR", "", 10)
        pdf.cell(50, 10, "--------------------------------------------------------------------------------------------", ln=True)
        pdf.cell(100, 10, "БИЛЕТ", ln=True, align="C")
        pdf.cell(50, 10, "--------------------------------------------------------------------------------------------", ln=True)
        pdf.cell(50, 10, "Номер клиента:")
        pdf.cell(50, 10, str(ammountcl), ln=True)
        pdf.cell(50, 10, "Номер экскурсии:")
        pdf.cell(50, 10, str(ammountex), ln=True)
        pdf.cell(50, 10, "Фамилия:")
        pdf.cell(50, 10, self.lineEdit_2.text(), ln=True)
        pdf.cell(50, 10, "Имя:")
        pdf.cell(50, 10, self.lineEdit.text(), ln=True)
        pdf.cell(50, 10, "Телефон:")
        pdf.cell(50, 10, str(self.lineEdit_3.text()), ln=True)
        pdf.cell(50, 10, "Тип экскурсии:")
        pdf.cell(50, 10, type, ln=True)
        pdf.cell(50, 10, "Длительность:")
        pdf.cell(50, 10, self.lineEdit_5.text(), ln=True)
        pdf.cell(50, 10, "Количество человек:")
        pdf.cell(50, 10, str(self.lineEdit_4.text()), ln=True)
        pdf.cell(50, 10, "Цена на человека:")
        pdf.cell(50, 10, price, ln=True)
        pdf.cell(50, 10, "Дата экскурсии:")
        pdf.cell(50, 10, self.comboBox.currentText(), ln=True)
        pdf.cell(50, 10, "--------------------------------------------------------------------------------------------", ln=True)
        pdf.cell(50, 10, "Суммарная стоимость:")
        sum = float(price) * float(self.lineEdit_4.text())
        pdf.cell(50, 10, str(sum), ln=True)
        pdf.cell(50, 10, "--------------------------------------------------------------------------------------------", ln=True)
        pdf.output("Ticket.pdf")
        Ticket = QMessageBox()
        Ticket.setWindowTitle("Билет создан")
        Ticket.setText("Он размещен в той же папке, в которой находится программа")
        Ticket.exec_()
    def check(self):
        if self.radioButton.isChecked():
            self.comboBox.clear()
            T = datetime.datetime.today()
            T = datetime.datetime(T.year, T.month, T.day, 10)
            for i in range(5):
                for j in range(10):
                    self.comboBox.addItem(str(T))
                    if (int(T.hour) == 24):
                        T = datetime.datetime(T.year, T.month, T.day + 1, 1)
                    else:
                        T = datetime.datetime(T.year, T.month, T.day, T.hour+ 1)
                if (int(T.day) == 31):
                    T = datetime.datetime(T.year, T.month + 1, 1, 10)
                else:
                    T = datetime.datetime(T.year, T.month, T.day + 1, 10)
        else:
            T = datetime.date.today()
            T = datetime.datetime(T.year, T.month, T.day, 12)
            self.comboBox.clear()
            for i in range(5):
                self.comboBox.addItem(str(T))
                if (int(T.day) == 31):
                    T = datetime.datetime(T.year, T.month + 1, 1, T.hour)
                else:
                    T = datetime.datetime(T.year, T.month, T.day + 1, T.hour)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Бронь"))
        self.label.setText(_translate("Form", "Для записи на плановую экскурсию или бронирования частной экскурсии необходимо заполнить следующую форму:"))
        self.pushButton.setText(_translate("Form", "Ок"))
        self.label_2.setText(_translate("Form", "Имя"))
        self.label_3.setText(_translate("Form", "Фамилия"))
        self.label_4.setText(_translate("Form", "Телефон"))
        self.label_5.setText(_translate("Form", "Количество человек"))
        self.label_6.setText(_translate("Form", "Дата экскурсии"))
        self.label_7.setText(_translate("Form", "Тип экскурсии"))
        self.label_10.setText(_translate("Form", "Длительность"))
        self.label_11.setText(_translate("Form", "Номера залов"))
        self.radioButton.setText(_translate("Form", "Заказная"))
        self.checkBox.setText(_translate("Form", "1A"))
        self.checkBox_2.setText(_translate("Form", "1B"))
        self.checkBox_3.setText(_translate("Form", "1C"))