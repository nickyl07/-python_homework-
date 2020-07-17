from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os
import pymysql

class Ui_re_user(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_re_user,self).__init__()
        self.setupUi(self)

    def setupUi(self, re_user):
        re_user.setObjectName("re_user")
        re_user.resize(361, 335)
        self.DZJM = QtWidgets.QLabel(re_user)
        self.DZJM.setGeometry(QtCore.QRect(90, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.DZJM.setFont(font)
        self.DZJM.setObjectName("DZJM")
        self.pushButton_2 = QtWidgets.QPushButton(re_user)
        self.pushButton_2.setGeometry(QtCore.QRect(210, 290, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton = QtWidgets.QPushButton(re_user)
        self.pushButton.setGeometry(QtCore.QRect(70, 290, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.formLayoutWidget_2 = QtWidgets.QWidget(re_user)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(70, 110, 231, 161))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Label = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Label.setObjectName("Label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Label)
        self.ID = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.ID.setObjectName("ID")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.ID)
        self.Label_5 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Label_5.setObjectName("Label_5")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.Label_5)
        self.amdin = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.amdin.setObjectName("amdin")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.amdin)
        self.Label_6 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Label_6.setObjectName("Label_6")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.Label_6)
        self.password = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.password.setObjectName("password")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.password)
        self.Label_7 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Label_7.setObjectName("Label_7")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.Label_7)
        self.role = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.role.setObjectName("role")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.role)
        self.Label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.Label_8.setObjectName("Label_8")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.Label_8)
        self.email = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.email.setObjectName("email")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.email)

        self.retranslateUi(re_user)
        self.pushButton.clicked.connect(self.user_modify)
        self.pushButton_2.clicked.connect(re_user.close)
        QtCore.QMetaObject.connectSlotsByName(re_user)
        self.amdin.returnPressed.connect(self.user_modify)
        self.email.returnPressed.connect(self.user_modify)
        self.ID.returnPressed.connect(self.user_modify)
        self.role.returnPressed.connect(self.user_modify)
        self.password.returnPressed.connect(self.user_modify)

    def retranslateUi(self, re_user):
        _translate = QtCore.QCoreApplication.translate
        re_user.setWindowTitle(_translate("re_user", "修改读者信息"))
        self.DZJM.setText(_translate("re_user", "修改读者信息"))
        self.pushButton_2.setText(_translate("re_user", "退出"))
        self.pushButton.setText(_translate("re_user", "确定"))
        self.Label.setText(_translate("re_user", "ID"))
        self.Label_5.setText(_translate("re_user", "用户名"))
        self.Label_6.setText(_translate("re_user", "密码"))
        self.Label_7.setText(_translate("re_user", "权限"))
        self.Label_8.setText(_translate("re_user", "email"))

    def user_modify(self):
        id=self.ID.text()
        admin = self.amdin.text()
        email = self.email.text()
        password = self.password.text()
        role=self.role.text()   

        if (id == "" or admin == "" or email=="" or password=="" or role==""):
            print(QMessageBox.information(self, "提示", "输入数值不能为空", QMessageBox.Yes))            
        else:
            conn = pymysql.connect(host="localhost", user="root", password="123", database="admin", port=3306)
            # 获取游标 对数据库进行操作 并且将返回值设置为字典类型
            cur = conn.cursor()
            sql = "update user set admin='%s',email='%s',password='%s',role='%s' where id='%s'"

            flag=cur.execute(sql % (admin, email, password,role,id))
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
    mainMindow = Ui_re_user()
    mainMindow.show()
    sys.exit(app.exec_())