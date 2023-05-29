import pymongo
db_client = pymongo.MongoClient("mongodb://localhost:27017/")
current_db = db_client["museum"]
collection = current_db["Weapon"]
from seventh import Ui_Form6
from PyQt5 import QtCore, QtGui, QtWidgets
table = 0
class Ui_Form5(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1200, 800)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 1180, 750))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(9)
        self.tableWidget.setRowCount(0)
        item_0 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item_0)
        item_1 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item_1)
        item_2 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item_2)
        item_3 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item_3)
        item_4 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item_4)
        item_5 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item_5)
        item_6 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item_6)
        item_7 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item_7)
        item_8 = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item_8)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 760, 75, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(90, 760, 75, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(170, 760, 75, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(250, 760, 75, 30))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(Form)
        self.pushButton_5.setGeometry(QtCore.QRect(960, 760, 75, 30))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(Form)
        self.pushButton_6.setGeometry(QtCore.QRect(1040, 760, 75, 30))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(Form)
        self.pushButton_7.setGeometry(QtCore.QRect(1120, 760, 75, 30))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(Form)
        self.pushButton_8.setGeometry(QtCore.QRect(880, 760, 75, 30))
        self.pushButton_8.setObjectName("pushButton_8")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        self.pushButton.clicked.connect(self.FT)
        self.pushButton_2.clicked.connect(self.ST)
        self.pushButton_3.clicked.connect(self.TT)
        self.pushButton_4.clicked.connect(self.FoT)
        self.pushButton_5.clicked.connect(self.insert)
        self.pushButton_6.clicked.connect(self.delete)
        self.pushButton_7.clicked.connect(self.update)
        self.pushButton_8.clicked.connect(self.docs)
    def docs(self):
        self.Form6 = QtWidgets.QWidget()
        self.ui = Ui_Form6()
        self.ui.setupUi(self.Form6)
        self.Form6.setStyleSheet("#Form{background-color:white}")
        self.Form6.show()
    def insert(self):
        match table:
            case 1:
                collection = current_db["Weapon"]
                new = {
                    "name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                    "type": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "attack type": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                    "year": int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                    "location": self.tableWidget.item(self.tableWidget.currentRow(), 4).text(),
                    "source": self.tableWidget.item(self.tableWidget.currentRow(), 5).text(),
                    "price": int(self.tableWidget.item(self.tableWidget.currentRow(), 6).text()),
                    "description": self.tableWidget.item(self.tableWidget.currentRow(), 7).text()
                }
                collection.insert_one(new)
                self.FT()
            case 2:
                collection = current_db["Excursion"]
                new = {
                    "number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                    "type": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "duration": int(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()),
                    "guide service number": int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                    "halls": self.tableWidget.item(self.tableWidget.currentRow(), 4).text(),
                    "price per person": str(self.tableWidget.item(self.tableWidget.currentRow(), 5).text()),
                    "clients ammount": int(self.tableWidget.item(self.tableWidget.currentRow(), 6).text()),
                    "date": self.tableWidget.item(self.tableWidget.currentRow(), 7).text(),
                    "client numbers": self.tableWidget.item(self.tableWidget.currentRow(), 8).text()
                }
                collection.insert_one(new)
                self.ST()
            case 3:
                collection = current_db["Client"]
                new = {
                    "client number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                    "first name": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "second name": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                    "phone number": int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                    "ammount": int(self.tableWidget.item(self.tableWidget.currentRow(), 4).text()),
                    "date of visit": self.tableWidget.item(self.tableWidget.currentRow(), 5).text(),
                    "excursion number": int(self.tableWidget.item(self.tableWidget.currentRow(), 6).text())
                }
                collection.insert_one(new)
                self.TT()
            case 4:
                collection = current_db["Employee"]
                new = {
                    "service number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                    "first name": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                    "second name": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                    "post": self.tableWidget.item(self.tableWidget.currentRow(), 3).text(),
                    "salary": int(self.tableWidget.item(self.tableWidget.currentRow(), 4).text())
                }
                collection.insert_one(new)
                self.FoT()
    def delete(self):
        currentitem = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        match table:
            case 1:
                collection = current_db["Weapon"]
                collection.delete_one({"name": str(currentitem)})
                self.FT()
            case 2:
                collection = current_db["Excursion"]
                collection.delete_one({"number": int(currentitem)})
                self.ST()
            case 3:
                collection = current_db["Client"]
                collection.delete_one({"client number": int(currentitem)})
                self.TT()
            case 4:
                collection = current_db["Employee"]
                collection.delete_one({"service number": int(currentitem)})
                self.FoT()
    def update(self):
        currentitem = self.tableWidget.item(self.tableWidget.currentRow(), 0).text()
        match table:
            case 1:
                collection = current_db["Weapon"]
                collection.update_many({"name": str(currentitem)}, {
                    "$set": {"name": self.tableWidget.item(self.tableWidget.currentRow(), 0).text(),
                            "type": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                            "attack type": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                            "year": int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                            "location": self.tableWidget.item(self.tableWidget.currentRow(), 4).text(),
                            "source": self.tableWidget.item(self.tableWidget.currentRow(), 5).text(),
                            "price": int(self.tableWidget.item(self.tableWidget.currentRow(), 6).text()),
                            "description": self.tableWidget.item(self.tableWidget.currentRow(), 7).text()}})
                self.FT()
            case 2:
                collection = current_db["Excursion"]
                collection.update_many({"number": int(currentitem)}, {
                    "$set": {"number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                             "type": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                             "duration": int(self.tableWidget.item(self.tableWidget.currentRow(), 2).text()),
                             "guide service number": int(
                                 self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                             "halls": self.tableWidget.item(self.tableWidget.currentRow(), 4).text(),
                             "price per person": str(
                                 self.tableWidget.item(self.tableWidget.currentRow(), 5).text()),
                             "clients ammount": int(self.tableWidget.item(self.tableWidget.currentRow(), 6).text()),
                             "date": self.tableWidget.item(self.tableWidget.currentRow(), 7).text(),
                             "client numbers": self.tableWidget.item(self.tableWidget.currentRow(), 8).text()}})
                self.ST()
            case 3:
                collection = current_db["Client"]
                collection.update_many({"client number": int(currentitem)}, {
                    "$set": {"client number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                             "first name": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                             "second name": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                             "phone number": int(self.tableWidget.item(self.tableWidget.currentRow(), 3).text()),
                             "ammount": int(self.tableWidget.item(self.tableWidget.currentRow(), 4).text()),
                             "date of visit": self.tableWidget.item(self.tableWidget.currentRow(), 5).text(),
                             "excursion number": int(
                             self.tableWidget.item(self.tableWidget.currentRow(), 6).text())}})
                self.TT()
            case 4:
                collection = current_db["Employee"]
                collection.update_many({"service number": int(currentitem)}, {
                    "$set": {"service number": int(self.tableWidget.item(self.tableWidget.currentRow(), 0).text()),
                             "first name": self.tableWidget.item(self.tableWidget.currentRow(), 1).text(),
                             "second name": self.tableWidget.item(self.tableWidget.currentRow(), 2).text(),
                             "post": self.tableWidget.item(self.tableWidget.currentRow(), 3).text(),
                             "salary": int(self.tableWidget.item(self.tableWidget.currentRow(), 4).text())}})
                self.FoT()
    def FT(self):
        global table
        table = 1
        self.chose()
        collection = current_db["Weapon"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(147)
        row = 0
        for Weapon in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Weapon["name"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Weapon["type"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Weapon["attack type"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Weapon["year"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Weapon["location"])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(Weapon["source"])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Weapon["price"])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(Weapon["description"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def ST(self):
        global table
        table = 2
        self.chose()
        collection = current_db["Excursion"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(130)
        row = 0
        for Excursion in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Excursion["number"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Excursion["type"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Excursion["duration"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Excursion["guide service number"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Excursion["halls"])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(Excursion["price per person"])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Excursion["clients ammount"])))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(Excursion["date"])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(Excursion["client numbers"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def TT(self):
        global table
        table = 3
        self.chose()
        collection = current_db["Client"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(168)
        row = 0
        for Client in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Client["client number"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Client["first name"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Client["second name"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Client["phone number"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Client["ammount"])))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(Client["date of visit"])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(Client["excursion number"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def FoT(self):
        global table
        table = 4
        self.chose()
        collection = current_db["Employee"]
        self.tableWidget.horizontalHeader().setDefaultSectionSize(236)
        row = 0
        self.tableWidget.setRowCount(row + 1)
        for Employee in collection.find():
            self.tableWidget.setRowCount(row + 1)
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(Employee["service number"])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(Employee["first name"])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(Employee["second name"])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(str(Employee["post"])))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(Employee["salary"])))
            row += 1
        self.tableWidget.setRowCount(row + 1)
    def chose(self):
        _translate = QtCore.QCoreApplication.translate
        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)
        item_3 = self.tableWidget.horizontalHeaderItem(3)
        item_4 = self.tableWidget.horizontalHeaderItem(4)
        item_5 = self.tableWidget.horizontalHeaderItem(5)
        item_6 = self.tableWidget.horizontalHeaderItem(6)
        item_7 = self.tableWidget.horizontalHeaderItem(7)
        item_8 = self.tableWidget.horizontalHeaderItem(8)
        match table:
            case 1:
                item_0.setText(_translate("Form", "Название"))
                item_1.setText(_translate("Form", "Тип"))
                item_2.setText(_translate("Form", "Тип атаки"))
                item_3.setText(_translate("Form", "Год"))
                item_4.setText(_translate("Form", "Расположение"))
                item_5.setText(_translate("Form", "Источник"))
                item_6.setText(_translate("Form", "Цена"))
                item_7.setText(_translate("Form", "Описание"))
            case 2:
                item_0.setText(_translate("Form", "Номер"))
                item_1.setText(_translate("Form", "Тип"))
                item_2.setText(_translate("Form", "Длительность"))
                item_3.setText(_translate("Form", "Экскурсовод"))
                item_4.setText(_translate("Form", "Залы"))
                item_5.setText(_translate("Form", "Цена на человека"))
                item_6.setText(_translate("Form", "Количество человек"))
                item_7.setText(_translate("Form", "Дата"))
                item_8.setText(_translate("Form", "Номера клиентов"))
            case 3:
                item_0.setText(_translate("Form", "Номер"))
                item_1.setText(_translate("Form", "Имя"))
                item_2.setText(_translate("Form", "Фамилия"))
                item_3.setText(_translate("Form", "Телефон"))
                item_4.setText(_translate("Form", "Количество человек"))
                item_5.setText(_translate("Form", "Дата посещения"))
                item_6.setText(_translate("Form", "Номер экскурсии"))
            case 4:
                item_0.setText(_translate("Form", "Табельный номер"))
                item_1.setText(_translate("Form", "Имя"))
                item_2.setText(_translate("Form", "Фамилия"))
                item_3.setText(_translate("Form", "Пост"))
                item_4.setText(_translate("Form", "Зарплата"))
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Окно администратора"))
        self.pushButton.setText(_translate("Form", "Экспонаты"))
        self.pushButton_2.setText(_translate("Form", "Экскурсии"))
        self.pushButton_3.setText(_translate("Form", "Клиенты"))
        self.pushButton_4.setText(_translate("Form", "Сотрудники"))
        self.pushButton_5.setText(_translate("Form", "Вставить"))
        self.pushButton_6.setText(_translate("Form", "Удалить"))
        self.pushButton_7.setText(_translate("Form", "Изменить"))
        self.pushButton_8.setText(_translate("Form", "Документы"))
        item_0 = self.tableWidget.horizontalHeaderItem(0)
        item_1 = self.tableWidget.horizontalHeaderItem(1)
        item_2 = self.tableWidget.horizontalHeaderItem(2)
        item_3 = self.tableWidget.horizontalHeaderItem(3)
        item_4 = self.tableWidget.horizontalHeaderItem(4)
        item_5 = self.tableWidget.horizontalHeaderItem(5)
        item_6 = self.tableWidget.horizontalHeaderItem(6)
        item_7 = self.tableWidget.horizontalHeaderItem(7)
        item_8 = self.tableWidget.horizontalHeaderItem(8)