from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_del_name(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_del_name,self).__init__()
        self.setupUi(self)

    def setupUi(self, del_name):
        del_name.setObjectName("del_name")
        del_name.resize(365, 336)
        self.DZJM = QtWidgets.QLabel(del_name)
        self.DZJM.setGeometry(QtCore.QRect(120, 40, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")
        self.formLayoutWidget = QtWidgets.QWidget(del_name)
        self.formLayoutWidget.setGeometry(QtCore.QRect(60, 110, 231, 71))
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
        self.pushButton = QtWidgets.QPushButton(del_name)
        self.pushButton.setGeometry(QtCore.QRect(60, 210, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(del_name)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 210, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(del_name)
        self.pushButton_2.clicked.connect(del_name.close)
        QtCore.QMetaObject.connectSlotsByName(del_name)
        self.pushButton.clicked.connect(self.name_delete)
        self.BID.returnPressed.connect(self.name_delete)
        self.name.returnPressed.connect(self.name_delete)


    def name_delete(self):
        id = self.BID.text()
        admin = self.name.text()
        if (id=="" or admin==""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))            
        else:            
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            cur = conn.cursor()
            sql = "delete from book where id = '%s' and admin='%s'"
            flag=cur.execute(sql%(id,admin))
            conn.commit()
            conn.close()  # 关闭连接  
            self.close()
            if flag==1:
                print(QMessageBox.information(self, "提示", "删除成功!", QMessageBox.Yes))
            else:
                print(QMessageBox.information(self, "提示", "输入错误!", QMessageBox.Yes))

    def retranslateUi(self, del_name):
        _translate = QtCore.QCoreApplication.translate
        del_name.setWindowTitle(_translate("del_name", "删除读者"))
        self.DZJM.setText(_translate("del_name", "删除读者"))
        self.Label.setText(_translate("del_name", "ID"))
        self.Label_2.setText(_translate("del_name", "用户名"))
        self.pushButton.setText(_translate("del_name", "确定"))
        self.pushButton_2.setText(_translate("del_name", "退出"))

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_del_name()
    mainMindow.show()
    sys.exit(App.exec_())