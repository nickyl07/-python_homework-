from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_New(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_New,self).__init__()
        self.setupUi(self)
        self.Newview()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(680, 463)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(260, 10, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(0, 60, 681, 411))
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

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "新书推荐"))
        self.label.setText(_translate("Form", "新书推荐"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Form", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Form", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Form", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Form", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Form", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Form", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Form", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Form", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Form", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Form", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Form", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Form", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Form", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Form", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Form", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Form", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Form", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Form", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Form", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Form", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "BID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "书名"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "作者"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "出版社"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "数量"))

    def Newview(self):
        # 数据库连接对象
        conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
        # 游标对象
        cur = conn.cursor()
        
        # 查询的sql语句
        sql = "SELECT * FROM book ORDER BY BID DESC"
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
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_New()
    mainMindow.show()
    sys.exit(app.exec_())