import pymongo
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["museum"]
collection = current_db["Excursion"]
import datetime
from fpdf import FPDF
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form6(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(300, 100)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 181, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(120, 10, 170, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Отчет по экскурсиям")
        self.comboBox.addItem("Отчет по посещениям")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(10, 50, 140, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        Excursion = collection.find()[0]
        max = datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S')
        min = datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S')
        for Excursion in collection.find():
            if datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S') > max:
                max = datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S')
            if datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S') < min:
                min = datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S')
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(150, 50, 140, 22))
        self.comboBox_3.setObjectName("comboBox_3")
        while 1:
            self.comboBox_2.addItem(str(min))
            self.comboBox_3.addItem(str(min))
            if (int(min.day) == 31):
                min = datetime.datetime(min.year, min.month + 1, 1, min.hour)
            else:
                min = datetime.datetime(min.year, min.month, min.day + 1, min.hour)
            if int(max.year) <= int(min.year) and int(max.month) <= int(min.month) and int(max.day) <= int(min.day):
                self.comboBox_2.addItem(str(min))
                self.comboBox_3.addItem(str(min))
                break
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(90, 75, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.doc)
    def doc(self):
        if self.comboBox.currentText() == "Отчет по экскурсиям":
            pdf = FPDF("P", "mm", "A4")
            pdf.add_page()
            pdf.add_font("TimesNR", "", "timesnrcyrmt.ttf", uni=True)
            pdf.set_font("TimesNR", "", 10)
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.cell(190, 10, "ОТЧЕТ ПО ЭКСКУРСИЯМ", ln=True, align="C")
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.cell(50, 10, "Промежуток времени:")
            pdf.cell(30, 10, self.comboBox_2.currentText())
            pdf.cell(3, 10, " -")
            pdf.cell(30, 10, self.comboBox_3.currentText(), ln=True)
            kolexp = 0
            kolexr = 0
            sumdur = 0
            kolcl = 0
            kolpr = 0
            kolexp = 0
            for Excursion in collection.find():
                if datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S') >= datetime.datetime.strptime(self.comboBox_2.currentText(), '%Y-%m-%d %H:%M:%S') and datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S') <= datetime.datetime.strptime(self.comboBox_3.currentText(), '%Y-%m-%d %H:%M:%S'):
                    if(Excursion["type"] == "planned"):
                        kolexp += 1
                    if (Excursion["type"] == "registered"):
                        kolexr += 1
                    sumdur += int(Excursion["duration"])
                    kolcl += int(Excursion["clients ammount"])
                    kolpr += float(Excursion["clients ammount"]) * float(Excursion["price per person"])
            pdf.cell(70, 10, "Количество планорвых экскурсий:")
            pdf.cell(70, 10, str(kolexp), ln=True)
            pdf.cell(70, 10, "Количество заказных экскурсий:")
            pdf.cell(70, 10, str(kolexr), ln=True)
            pdf.cell(70, 10, "Суммарная длительность:")
            pdf.cell(70, 10, str(sumdur), ln=True)
            pdf.cell(70, 10, "Количество клиентов:")
            pdf.cell(70, 10, str(kolcl), ln=True)
            pdf.cell(70, 10, "Количество прибыли:")
            pdf.cell(70, 10, str(kolpr), ln=True)
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.output("Reporte.pdf")
        elif self.comboBox.currentText() == "Отчет по посещениям":
            pdf = FPDF("P", "mm", "A4")
            pdf.add_page()
            pdf.add_font("TimesNR", "", "timesnrcyrmt.ttf", uni=True)
            pdf.set_font("TimesNR", "", 10)
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.cell(190, 10, "ОТЧЕТ ПО ПОСЕЩЕНИЯМ", ln=True, align="C")
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.cell(50, 10, "Промежуток времени:")
            pdf.cell(30, 10, self.comboBox_2.currentText())
            pdf.cell(3, 10, " -")
            pdf.cell(30, 10, self.comboBox_3.currentText(), ln=True)
            kolcl = 0
            kolpe = []
            for Excursion in collection.find():
                if datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S') >= datetime.datetime.strptime(
                        self.comboBox_2.currentText(), '%Y-%m-%d %H:%M:%S') and datetime.datetime.strptime(
                        Excursion["date"], '%Y-%m-%d %H:%M:%S') <= datetime.datetime.strptime(
                        self.comboBox_3.currentText(), '%Y-%m-%d %H:%M:%S'):
                    kolcl += int(Excursion["clients ammount"])
                    kolpe.extend(Excursion["client numbers"])
            kolpe = list(set(kolpe))
            i = 0
            while i <len(kolpe):
                if kolpe[i] == "[" or kolpe[i] == "]":
                    kolpe.pop(i)
                i += 1
            pdf.cell(70, 10, "Количество человек:")
            pdf.cell(70, 10, str(kolcl), ln=True)
            pdf.cell(70, 10, "Список клиентов:")
            pdf.cell(70, 10, str(kolpe), ln=True)
            pdf.cell(50, 10, "----------------------------------------------------------------------------------------------------------------------------------------------------------------", ln=True)
            pdf.output("Reportc.pdf")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Документы"))
        self.label.setText(_translate("Form", "Выберете документ"))
        self.label_2.setText(_translate("Form", "Выберете временной промежуток"))
        self.pushButton.setText(_translate("Form", "Ок"))