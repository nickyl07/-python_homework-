from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_back_book(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_back_book,self).__init__()
        self.setupUi(self)

    def setupUi(self, back_book):
        back_book.setObjectName("back_book")
        back_book.resize(366, 337)
        self.DZJM = QtWidgets.QLabel(back_book)
        self.DZJM.setGeometry(QtCore.QRect(120, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")
        self.formLayoutWidget = QtWidgets.QWidget(back_book)
        self.formLayoutWidget.setGeometry(QtCore.QRect(70, 110, 231, 71))
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
        self.pushButton = QtWidgets.QPushButton(back_book)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(back_book)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(back_book)
        self.pushButton.clicked.connect(self.book_modify)
        self.pushButton_2.clicked.connect(back_book.close)
        QtCore.QMetaObject.connectSlotsByName(back_book)

    def retranslateUi(self, back_book):
        _translate = QtCore.QCoreApplication.translate
        back_book.setWindowTitle(_translate("back_book", "归还图书"))
        self.DZJM.setText(_translate("back_book", "归还图书"))
        self.Label.setText(_translate("back_book", "BID"))
        self.Label_2.setText(_translate("back_book", "书名"))
        self.pushButton.setText(_translate("back_book", "确定"))
        self.pushButton_2.setText(_translate("back_book", "退出"))

    def book_modify(self):
        bid = self.BID.text()
        name = self.name.text() 
        conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
        cur = conn.cursor()        
        if (bid == "" or name == ""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))            
        else:
            sql = "update book set count=count+1 where bid='%s'"
            flag=cur.execute(sql % (bid))
            conn.commit()
            self.close()
            if flag==1:
                print(QMessageBox.information(self, "提示", "回还成功!", QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, "提示", "输入错误!", QMessageBox.Yes))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_back_book()
    mainMindow.show()
    sys.exit(app.exec_())