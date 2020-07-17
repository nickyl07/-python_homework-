from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_register(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_register,self).__init__()
        self.setupUi(self)

    def setupUi(self, register):
        register.setObjectName("register")
        register.resize(364, 336)
        self.pushButton = QtWidgets.QPushButton(register)
        self.pushButton.setGeometry(QtCore.QRect(60, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget = QtWidgets.QWidget(register)
        self.formLayoutWidget.setGeometry(QtCore.QRect(50, 100, 271, 161))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.Label = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label.setObjectName("Label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.ID = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.ID.setObjectName("ID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.Label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_2.setObjectName("Label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_2)
        self.admin = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.admin.setObjectName("admin")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.admin)
        self.Label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_3.setObjectName("Label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_3)
        self.passwd = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwd.setObjectName("passwd")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.passwd)
        self.Label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_4.setObjectName("Label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_4)
        self.passwd2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.passwd2.setObjectName("passwd2")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.passwd2)
        self.Label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.Label_5.setObjectName("Label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.email = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.email.setObjectName("email")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email)
        self.pushButton_2 = QtWidgets.QPushButton(register)
        self.pushButton_2.setGeometry(QtCore.QRect(200, 290, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.DZJM = QtWidgets.QLabel(register)
        self.DZJM.setGeometry(QtCore.QRect(150, 50, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")

        self.retranslateUi(register)
        self.pushButton.clicked.connect(self.user_insert)
        self.pushButton_2.clicked.connect(register.close)
        QtCore.QMetaObject.connectSlotsByName(register)

    def retranslateUi(self, register):
        _translate = QtCore.QCoreApplication.translate
        register.setWindowTitle(_translate("register_2", "注册"))
        self.pushButton.setText(_translate("register_2", "确定"))
        self.Label.setText(_translate("register_2", "学号（ID）"))
        self.Label_2.setText(_translate("register_2", "用户名"))
        self.Label_3.setText(_translate("register_2", "密码"))
        self.Label_4.setText(_translate("register_2", "重新输入密码"))
        self.Label_5.setText(_translate("register_2", "邮箱"))
        self.pushButton_2.setText(_translate("register_2", "退出"))
        self.DZJM.setText(_translate("register_2", "注册"))

    def user_insert(self):
        id = self.ID.text()
        admin = self.admin.text()
        password = self.passwd.text()
        password2 = self.passwd2.text()
        email = self.email.text()  
        role=0
        if (id == "" or admin == "" or password=="" or password2=="" or email==""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))
        elif(password!=password2):
            print(QMessageBox.information(self, "提示", "密码不一致", QMessageBox.Yes))            
        else:
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
            cur = conn.cursor()
            # 写sql语句
            sql = "insert into user(id,admin,password,role,email) values('%s','%s','%s','%s','%s')"

            try:
                cur.execute(sql % (id,admin,password,role,email))
                conn.commit()
            except Exception as e:
                # 错误回滚
                conn.rollback()
                raise e
            finally:
                conn.close()  # 关闭连接  
            self.close()
            print(QMessageBox.information(self, "提示", "注册成功!", QMessageBox.Yes))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_register()
    mainMindow.show()
    sys.exit(app.exec_())
