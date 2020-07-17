from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_re_book(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_re_book,self).__init__()
        self.setupUi(self)

    def setupUi(self, re_book):
        re_book.setObjectName("re_book")
        re_book.resize(365, 336)
        self.DZJM = QtWidgets.QLabel(re_book)
        self.DZJM.setGeometry(QtCore.QRect(100, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")
        self.formLayoutWidget = QtWidgets.QWidget(re_book)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 110, 231, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.BID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.BID.setObjectName("BID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.BID)
        self.Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.name)
        self.Label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.author = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.author.setObjectName("author")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.author)
        self.Label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.press = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.press.setObjectName("press")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.press)
        self.Label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.count = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.count.setObjectName("count")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.count)
        self.pushButton = QtWidgets.QPushButton(re_book)
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(re_book)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(re_book)
        self.pushButton_2.clicked.connect(re_book.close)
        self.pushButton.clicked.connect(self.book_modify)
        QtCore.QMetaObject.connectSlotsByName(re_book)
        self.BID.returnPressed.connect(self.book_modify)
        self.name.returnPressed.connect(self.book_modify)
        self.press.returnPressed.connect(self.book_modify)
        self.author.returnPressed.connect(self.book_modify)
        self.count.returnPressed.connect(self.book_modify)


    def retranslateUi(self, re_book):
        _translate = QtCore.QCoreApplication.translate
        re_book.setWindowTitle(_translate("re_book", "修改图书信息"))
        self.DZJM.setText(_translate("re_book", "修改图书信息"))
        self.Label.setText(_translate("re_book", "BID"))
        self.Label_2.setText(_translate("re_book", "书名"))
        self.Label_3.setText(_translate("re_book", "作者"))
        self.Label_4.setText(_translate("re_book", "出版社"))
        self.Label_5.setText(_translate("re_book", "数量"))
        self.pushButton.setText(_translate("re_book", "确定"))
        self.pushButton_2.setText(_translate("re_book", "退出"))

    def book_modify(self):
        bid = self.BID.text()
        namd = self.name.text()
        press = self.author.text()
        author = self.press.text()
        count=self.count.text()     
        if (bid == "" or name == "" or press=="" or author=="" or count==""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))            
        else:
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
            cur = conn.cursor()
            sql = "update book set name='%s',author='%s',press='%s',count='%s' where bid='%s'"

            flag=cur.execute(sql % (name, author, press,count,bid))
            conn.commit()
            self.close()
            if flag==1:
                print(QMessageBox.information(self, "提示", "更新成功!", QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, "提示", "输入错误!", QMessageBox.Yes))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_re_book()
    mainMindow.show()
    sys.exit(app.exec_())