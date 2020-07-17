from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import pymysql
from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os

class Ui_del_book(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_del_book,self).__init__()
        self.setupUi(self)

    def setupUi(self, del_book):
        del_book.setObjectName("del_book")
        del_book.resize(366, 338)
        self.DZJM = QtWidgets.QLabel(del_book)
        self.DZJM.setGeometry(QtCore.QRect(130, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")
        self.formLayoutWidget = QtWidgets.QWidget(del_book)
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
        self.pushButton = QtWidgets.QPushButton(del_book)
        self.pushButton.setGeometry(QtCore.QRect(70, 200, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(del_book)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 200, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(del_book)
        self.pushButton.clicked.connect(self.book_delete)
        self.pushButton_2.clicked.connect(del_book.close)
        QtCore.QMetaObject.connectSlotsByName(del_book)
        self.BID.returnPressed.connect(self.book_delete)
        self.name.returnPressed.connect(self.book_delete)

    def retranslateUi(self, del_book):
        _translate = QtCore.QCoreApplication.translate
        del_book.setWindowTitle(_translate("del_book", "删除图书"))
        self.DZJM.setText(_translate("del_book", "删除图书"))
        self.Label.setText(_translate("del_book", "BID"))
        self.Label_2.setText(_translate("del_book", "书名"))
        self.pushButton.setText(_translate("del_book", "确定"))
        self.pushButton_2.setText(_translate("del_book", "退出"))

    def book_delete(self):
        bid = self.BID.text()
        name = self.name.text()
        if (bid=="" or name==""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))            
        else:            
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            cur = conn.cursor()
            sql = "delete from book where bid = '%s' and name='%s'"
            flag=cur.execute(sql%(bid,name))
            conn.commit()
            conn.close()  # 关闭连接  
            self.close()
            if flag==1:
                print(QMessageBox.information(self, "提示", "删除成功!", QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, "提示", "输入错误!", QMessageBox.Yes))
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_del_book()
    mainMindow.show()
    sys.exit(app.exec_())