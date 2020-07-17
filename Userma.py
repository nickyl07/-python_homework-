from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from del_name import Ui_del_name
from re_user import Ui_re_user

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_Userma(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Userma,self).__init__()
        self.setupUi(self)
        self.Userview()

    def setupUi(self, Userma):
        Userma.setObjectName("Userma")
        Userma.resize(884, 599)
        self.GLYRK = QtWidgets.QLabel(Userma)
        self.GLYRK.setGeometry(QtCore.QRect(230, 100, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.GLYRK.setFont(font)
        self.GLYRK.setText("")
        self.GLYRK.setObjectName("GLYRK")
        self.tableWidget = QtWidgets.QTableWidget(Userma)
        self.tableWidget.setGeometry(QtCore.QRect(210, 120, 681, 481))
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
        self.pushButton_2 = QtWidgets.QPushButton(Userma)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 110, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Userma)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 180, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_5 = QtWidgets.QPushButton(Userma)
        self.pushButton_5.setGeometry(QtCore.QRect(40, 320, 93, 28))
        self.pushButton_5.setObjectName("pushButton_5")
        self.label = QtWidgets.QLabel(Userma)
        self.label.setGeometry(QtCore.QRect(370, 60, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.find_user_text = QtWidgets.QLineEdit(Userma)
        self.find_user_text.setGeometry(QtCore.QRect(340, 60, 471, 41))
        self.find_user_text.setObjectName("find_user_text")
        self.find_user_Button = QtWidgets.QPushButton(Userma)
        self.find_user_Button.setGeometry(QtCore.QRect(820, 60, 61, 41))
        self.find_user_Button.setObjectName("find_user_Button")
        self.find_user_comboBox = QtWidgets.QComboBox(Userma)
        self.find_user_comboBox.setGeometry(QtCore.QRect(210, 60, 121, 41))
        self.find_user_comboBox.setObjectName("find_user_comboBox")
        self.find_user_comboBox.addItem("")
        self.find_user_comboBox.addItem("")
        self.find_user_comboBox.addItem("")
        self.find_user_comboBox.addItem("")
        self.label_2 = QtWidgets.QLabel(Userma)
        self.label_2.setGeometry(QtCore.QRect(370, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.retranslateUi(Userma)
        QtCore.QMetaObject.connectSlotsByName(Userma)
        self.pushButton_5.clicked.connect(Userma.close)
        self.find_user_Button.clicked.connect(self.record)        
        self.pushButton_3.clicked.connect(self.onclick2)#修改        
        self.pushButton_2.clicked.connect(self.onclick)#删除

    def onclick(self):
        self.newWindow=Ui_del_name()
        self.newWindow.show()

    def onclick2(self):
        self.newWindow=Ui_re_user()
        self.newWindow.show()

    def retranslateUi(self, Userma):
        _translate = QtCore.QCoreApplication.translate
        Userma.setWindowTitle(_translate("Userma", "读者管理"))
        item = self.tableWidget.verticalHeaderItem(0)
        item.setText(_translate("Userma", "1"))
        item = self.tableWidget.verticalHeaderItem(1)
        item.setText(_translate("Userma", "2"))
        item = self.tableWidget.verticalHeaderItem(2)
        item.setText(_translate("Userma", "3"))
        item = self.tableWidget.verticalHeaderItem(3)
        item.setText(_translate("Userma", "4"))
        item = self.tableWidget.verticalHeaderItem(4)
        item.setText(_translate("Userma", "5"))
        item = self.tableWidget.verticalHeaderItem(5)
        item.setText(_translate("Userma", "6"))
        item = self.tableWidget.verticalHeaderItem(6)
        item.setText(_translate("Userma", "7"))
        item = self.tableWidget.verticalHeaderItem(7)
        item.setText(_translate("Userma", "8"))
        item = self.tableWidget.verticalHeaderItem(8)
        item.setText(_translate("Userma", "9"))
        item = self.tableWidget.verticalHeaderItem(9)
        item.setText(_translate("Userma", "10"))
        item = self.tableWidget.verticalHeaderItem(10)
        item.setText(_translate("Userma", "11"))
        item = self.tableWidget.verticalHeaderItem(11)
        item.setText(_translate("Userma", "12"))
        item = self.tableWidget.verticalHeaderItem(12)
        item.setText(_translate("Userma", "13"))
        item = self.tableWidget.verticalHeaderItem(13)
        item.setText(_translate("Userma", "14"))
        item = self.tableWidget.verticalHeaderItem(14)
        item.setText(_translate("Userma", "15"))
        item = self.tableWidget.verticalHeaderItem(15)
        item.setText(_translate("Userma", "16"))
        item = self.tableWidget.verticalHeaderItem(16)
        item.setText(_translate("Userma", "17"))
        item = self.tableWidget.verticalHeaderItem(17)
        item.setText(_translate("Userma", "18"))
        item = self.tableWidget.verticalHeaderItem(18)
        item.setText(_translate("Userma", "19"))
        item = self.tableWidget.verticalHeaderItem(19)
        item.setText(_translate("Userma", "20"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Userma", "ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Userma", "用户名"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Userma", "密码"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Userma", "权限"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Userma", "email"))
        self.pushButton_2.setText(_translate("Userma", "删除"))
        self.pushButton_3.setText(_translate("Userma", "修改"))
        self.pushButton_5.setText(_translate("Userma", "退出"))
        self.label.setText(_translate("Userma", "读者管理"))
        self.find_user_Button.setText(_translate("Userma", "查询"))
        self.find_user_comboBox.setItemText(0, _translate("Userma", "ID"))
        self.find_user_comboBox.setItemText(1, _translate("Userma", "用户名"))
        self.find_user_comboBox.setItemText(2, _translate("Userma", "email"))
        self.find_user_comboBox.setItemText(3, _translate("Userma", "权限"))
        self.label_2.setText(_translate("Userma", "读者管理"))

    # 查询
    def record(self, index):
        queryCondition = ""
        conditionChoice = self.find_user_comboBox.currentText()
        if (conditionChoice == "ID"):
            conditionChoice = 'id'
        elif (conditionChoice == "用户名"):
            conditionChoice = 'admin'
        elif (conditionChoice == "email"):
            conditionChoice = 'eamil'
        else:
            conditionChoice = 'role'

        if (self.find_user_text.text() == ""):
            self.tableWidget.clearContents()
            self.Userview()
        else:
            self.tableWidget.clearContents()
            temp =self.find_user_text.text()
            s = '%'
            for i in range(0, len(temp)):
                s = s + temp[i] + "%"
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            # 游标对象
            cur = conn.cursor()            
            sql="SELECT * FROM user WHERE %s LIKE '%s' ORDER BY %s " % (
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

    def Userview(self):
        # 数据库连接对象
        conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
        # 游标对象
        cur = conn.cursor()
        
        # 查询的sql语句
        sql = "SELECT * FROM user"
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
    mainMindow = Ui_Userma()
    mainMindow.show()
    sys.exit(app.exec_())