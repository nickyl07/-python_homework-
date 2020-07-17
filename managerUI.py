from Manager import Ui_Manager
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtSql import *

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys,os
import pymysql
#管理员入口
class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(170, 300, 93, 28))
        self.login.setObjectName("login")
        self.admin = QtWidgets.QLabel(Form)
        self.admin.setGeometry(QtCore.QRect(180, 170, 72, 15))
        self.admin.setObjectName("admin")
        self.password = QtWidgets.QLabel(Form)
        self.password.setGeometry(QtCore.QRect(180, 230, 72, 15))
        self.password.setObjectName("password")
        self.admin2 = QtWidgets.QLineEdit(Form)
        self.admin2.setGeometry(QtCore.QRect(270, 170, 151, 21))
        self.admin2.setObjectName("admin2")
        self.password2 = QtWidgets.QLineEdit(Form)
        self.password2.setGeometry(QtCore.QRect(270, 230, 151, 21))
        self.password2.setObjectName("password2")
        self.GLYRK = QtWidgets.QLabel(Form)
        self.GLYRK.setGeometry(QtCore.QRect(250, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.GLYRK.setFont(font)
        self.GLYRK.setObjectName("GLYRK")
        self.exit = QtWidgets.QPushButton(Form)
        self.exit.setGeometry(QtCore.QRect(350, 300, 93, 28))
        self.exit.setObjectName("exit")

        self.retranslateUi(Form)
        self.exit.clicked.connect(Form.close)
        self.login.clicked.connect(self.signInCheck)
        self.admin2.returnPressed.connect(self.signInCheck)
        self.password2.returnPressed.connect(self.signInCheck)

        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员入口"))
        self.login.setText(_translate("Form", "登录"))
        self.admin.setText(_translate("Form", "用户名"))
        self.password.setText(_translate("Form", "密码"))
        self.GLYRK.setText(_translate("Form", "管理员入口"))
        self.exit.setText(_translate("Form", "退出"))

    def signInCheck(self):
        studentId = self.admin2.text()
        password = self.password2.text()
        if (studentId == "" or password == ""):
            print(QMessageBox.warning(self, "警告", "学号和密码不可为空!",QMessageBox.Yes | QMessageBox.No,QMessageBox.Yes))
            return
        # 打开数据库连接
        connection=pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
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
                print(QMessageBox.information(self, "提示", "登陆成功!", QMessageBox.Yes))
                self.onclick()
                self.close()                                
            else:
                #读者界面
                print(QMessageBox.information(self, "提示", "你不是管理员!", QMessageBox.Yes,QMessageBox.Yes))
        return

    def onclick(self):
        self.newWindow=Ui_Manager()
        self.newWindow.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_Form()
    mainMindow.show()
    sys.exit(app.exec_())    