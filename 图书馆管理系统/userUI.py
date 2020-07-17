#读者入口
from Useruse import Ui_Useruse
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtSql import *
from register import Ui_register
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os
import pymysql

class Ui_Read(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Read):
        Read.setObjectName("Read")
        Read.resize(640, 480)
        self.DZRK = QtWidgets.QLabel(Read)
        self.DZRK.setGeometry(QtCore.QRect(270, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZRK.setFont(font)
        self.DZRK.setObjectName("DZRK")
        self.login = QtWidgets.QPushButton(Read)
        self.login.setGeometry(QtCore.QRect(350, 300, 93, 28))
        self.login.setObjectName("login")
        self.register = QtWidgets.QPushButton(Read)
        self.register.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.register.setObjectName("register")
        self.admin = QtWidgets.QLabel(Read)
        self.admin.setGeometry(QtCore.QRect(180, 170, 72, 15))
        self.admin.setObjectName("admin")
        self.password2 = QtWidgets.QLineEdit(Read)
        self.password2.setGeometry(QtCore.QRect(270, 230, 151, 21))
        self.password2.setObjectName("password2")
        self.admin2 = QtWidgets.QLineEdit(Read)
        self.admin2.setGeometry(QtCore.QRect(270, 170, 151, 21))
        self.admin2.setObjectName("admin2")
        self.password = QtWidgets.QLabel(Read)
        self.password.setGeometry(QtCore.QRect(180, 230, 72, 15))
        self.password.setObjectName("password")

        self.retranslateUi(Read)
        QtCore.QMetaObject.connectSlotsByName(Read)
        self.register.clicked.connect(self.onclick2)
        self.login.clicked.connect(self.signInCheck)
        self.admin2.returnPressed.connect(self.signInCheck)
        self.password2.returnPressed.connect(self.signInCheck)


    def retranslateUi(self, Read):
        _translate = QtCore.QCoreApplication.translate
        Read.setWindowTitle(_translate("Read", "Read"))
        self.DZRK.setText(_translate("Read", "读者入口"))
        self.login.setText(_translate("Read", "登录"))
        self.register.setText(_translate("Read", "注册"))
        self.admin.setText(_translate("Read", "用户名"))
        self.password.setText(_translate("Read", "密码"))

    def signInCheck(self):
        studentId = self.admin2.text()
        password = self.password2.text()
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "学号和密码不可为空!",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes))
            return
        # 打开数据库连接
        connection = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
        cur=connection.cursor()
        sql = """select * from user where  (id = %s) and (password = %s) """
        flag=cur.execute(sql,[studentId,password])
        connection.commit()
        if flag!=1:
            print(QMessageBox.information(self, "提示", "账号或密码不正确!", QMessageBox.Yes,QMessageBox.Yes))
        else:
            sql = """select * from user where (role = %s) """
            connection.commit()
            if cur.fetchone()[3]!=0:
                print(QMessageBox.information(self, "提示", "请从管理员入口登录!", QMessageBox.Yes,QMessageBox.Yes))

            else:
                print(QMessageBox.information(self, "提示", "登录成功!", QMessageBox.Yes))
                self.onclick()

        return

    def onclick(self):
        self.newWindow=Ui_Useruse()
        self.newWindow.show()      

    def onclick2(self):
        self.newWindow=Ui_register()
        self.newWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_Read()
    mainMindow.show()
    sys.exit(app.exec_()) 