from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql
from borrow_book import Ui_borrow_book
from back_book import Ui_back_book
from hot import Ui_Hot
from new import Ui_New

class Ui_Useruse(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Useruse,self).__init__()
        self.setupUi(self)
        self.Bookview()
        
    def setupUi(self, Useruse):
        Useruse.setObjectName("Useruse")
        Useruse.resize(884, 598)
        self.pushButton_2 = QtWidgets.QPushButton(Useruse)
        self.pushButton_2.setGeometry(QtCore.QRect(30, 170, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_5 = QtWidgets.QPushButton(Useruse)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 380, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.find_book_text = QtWidgets.QLineEdit(Useruse)
        self.find_book_text.setGeometry(QtCore.QRect(330, 70, 471, 41))
        self.find_book_text.setObjectName("find_book_text")
        self.GLYRK = QtWidgets.QLabel(Useruse)
        self.GLYRK.setGeometry(QtCore.QRect(220, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.GLYRK.setFont(font)
        self.GLYRK.setText("")
        self.GLYRK.setObjectName("GLYRK")
        self.tableWidget = QtWidgets.QTableWidget(Useruse)
        self.tableWidget.setGeometry(QtCore.QRect(200, 130, 681, 471))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(20)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(17, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(18, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(19, item)
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
        self.pushButton = QtWidgets.QPushButton(Useruse)
        self.pushButton.setGeometry(QtCore.QRect(30, 100, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(Useruse)
        self.pushButton_3.setGeometry(QtCore.QRect(30, 240, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.find_book_Button = QtWidgets.QPushButton(Useruse)
        self.find_book_Button.setGeometry(QtCore.QRect(810, 70, 61, 41))
        self.find_book_Button.setObjectName("find_book_Button")
        self.find_book_comboBox = QtWidgets.QComboBox(Useruse)
        self.find_book_comboBox.setGeometry(QtCore.QRect(200, 70, 121, 41))
        self.find_book_comboBox.setObjectName("find_book_comboBox")
        self.find_book_comboBox.addItem("")
        self.find_book_comboBox.addItem("")
        self.find_book_comboBox.addItem("")
        self.find_book_comboBox.addItem("")
        self.label = QtWidgets.QLabel(Useruse)
        self.label.setGeometry(QtCore.QRect(360, 20, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton_4 = QtWidgets.QPushButton(Useruse)
        self.pushButton_4.setGeometry(QtCore.QRect(30, 310, 93, 28))
        self.pushButton_4.setObjectName("pushButton_4")

        self.retranslateUi(Useruse)
        self.pushButton.clicked.connect(self.onclick)
        self.pushButton_2.clicked.connect(self.onclick2)
        self.pushButton_4.clicked.connect(self.onclick3)
        self.pushButton_3.clicked.connect(self.onclick4)
        self.pushButton_5.clicked.connect(Useruse.close)
        self.find_book_Button.clicked.connect(self.record)

        
        QtCore.QMetaObject.connectSlotsByName(Useruse)

    def onclick(self):
        self.newWindow=Ui_borrow_book()
        self.newWindow.show()      

    def onclick2(self):
        self.newWindow=Ui_back_book()
        self.newWindow.show()

    def onclick3(self):
        self.newWindow=Ui_Hot()
        self.newWindow.show()

    def onclick4(self):
        self.newWindow=Ui_New()
        self.newWindow.show()

    def retranslateUi(self, Useruse):
        _translate = QtCore.QCoreApplication.translate
        Useruse.setWindowTitle(_translate("Useruse", "Welcome"))
        self.pushButton_2.setText(_translate("Useruse", "归还"))
        self.pushButton_5.setText(_translate("Useruse", "退出"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Useruse", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Useruse", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Useruse", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Useruse", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Useruse", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Useruse", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Useruse", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Useruse", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Useruse", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Useruse", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Useruse", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Useruse", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Useruse", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Useruse", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Useruse", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Useruse", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Useruse", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Useruse", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Useruse", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Useruse", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Useruse", "BID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Useruse", "书名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Useruse", "作者"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Useruse", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Useruse", "数量"))
        self.pushButton.setText(_translate("Useruse", "借阅"))
        self.pushButton_3.setText(_translate("Useruse", "新书推荐"))
        self.find_book_Button.setText(_translate("Useruse", "查询"))
        self.find_book_comboBox.setItemText(0, _translate("Useruse", "BID"))
        self.find_book_comboBox.setItemText(1, _translate("Useruse", "书名"))
        self.find_book_comboBox.setItemText(2, _translate("Useruse", "作者"))
        self.find_book_comboBox.setItemText(3, _translate("Useruse", "出版社"))
        self.label.setText(_translate("Useruse", "Welcome to library!"))
        self.pushButton_4.setText(_translate("Useruse", "热书排行榜"))

    def record(self, index):
        queryCondition = ""
        conditionChoice = self.find_book_comboBox.currentText()
        if (conditionChoice == "BID"):
            conditionChoice = 'bid'
        elif (conditionChoice == "书名"):
            conditionChoice = 'name'
        elif (conditionChoice == "作者"):
            conditionChoice = 'author'
        else:
            conditionChoice = 'press'
#self.admin2.text()
        if (self.find_book_text.text() == ""):
            self.tableWidget.clearContents()
            self.Bookview()
        else:
            self.tableWidget.clearContents()
            temp =self.find_book_text.text()
            s = '%'
            for i in range(0, len(temp)):
                s = s + temp[i] + "%"
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            # 游标对象
            cur = conn.cursor()            
            sql="SELECT * FROM book WHERE %s LIKE '%s' ORDER BY %s " % (
            conditionChoice, s,conditionChoice)

            flag=cur.execute(sql)
            # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
            if flag==1:
                data = cur.fetchall()
                    # 打印测试
                print(data)
                    # print(data[0][1]) # 打印第1行第2个数据, 也就是小明

                    # 遍历二维元组, 将 id 和 name 显示到界面表格上
                x = 0
                for i in data:
                    y = 0
                    for j in i:
                        self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                        y = y + 1
                    x = x + 1
            else:
                print(QMessageBox.information(self, "提示", "该数据不存在!", QMessageBox.Yes,QMessageBox.Yes))

            cur.close()
            conn.close()       

    def Bookview(self):
        # 数据库连接对象
        conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
        # 游标对象
        cur = conn.cursor()
        
        # 查询的sql语句
        sql = "SELECT * FROM book"
        cur.execute(sql)
        # 获取查询到的数据, 是以二维元组的形式存储的, 所以读取需要使用 data[i][j] 下标定位
        data = cur.fetchall()
        # 打印测试
        print(data)
        # print(data[0][1]) # 打印第1行第2个数据, 也就是小明

        # 遍历二维元组, 将 id 和 name 显示到界面表格上
        x = 0
        for i in data:
            y = 0
            for j in i:
                self.tableWidget.setItem(x, y, QtWidgets.QTableWidgetItem(str(data[x][y])))
                y = y + 1
            x = x + 1

        cur.close()
        conn.close()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    mainMindow = Ui_Useruse()
    mainMindow.show()
    sys.exit(app.exec_())