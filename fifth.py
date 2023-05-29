import pymongo
import datetime
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["museum"]
collection = current_db["Excursion"]
from PyQt5 import QtCore, QtGui, QtWidgets
class Ui_Form4(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1000, 800)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 980, 780))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(140)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.loaddata()
    def loaddata(self):
        T = datetime.datetime.today()
        row = 0
        for Excursion in collection.find():
            T1 = datetime.datetime.strptime(Excursion["date"], '%Y-%m-%d %H:%M:%S')
            self.tableWidget.setRowCount(row + 1)
            if T1.year >= T.year:
                if T1.month >= T.month:
                    if T1.day >= T.day:
                        self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Excursion["number"])))
                        self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(Excursion["type"]))
                        self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(Excursion["duration"]))
                        self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Excursion["halls"])))
                        self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Excursion["price per person"])))
                        self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(Excursion["clients ammount"])))
                        self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Excursion["date"])))
                        row += 1
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Экскурсии"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Номер"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Тип"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Длительность"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Залы"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Цена на человека"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Количество человек"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Дата"))