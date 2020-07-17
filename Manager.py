from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from PyQt5 import QtCore, QtGui, QtWidgets
import sys,os

from Bookma import Ui_Bookma
from Userma import Ui_Userma

class Ui_Manager(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Manager,self).__init__()
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(640, 480)
        self.GLYRK = QtWidgets.QLabel(Form)
        self.GLYRK.setGeometry(QtCore.QRect(250, 90, 151, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.GLYRK.setFont(font)
        self.GLYRK.setObjectName("GLYRK")
        self.DZGL = QtWidgets.QPushButton(Form)
        self.DZGL.setGeometry(QtCore.QRect(260, 160, 93, 28))
        self.DZGL.setObjectName("DZGL")
        self.TSGL = QtWidgets.QPushButton(Form)
        self.TSGL.setGeometry(QtCore.QRect(260, 220, 93, 28))
        self.TSGL.setObjectName("TSGL")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 270, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(Form)
        self.pushButton_3.clicked.connect(Form.close)
        self.DZGL.clicked.connect(self.onclick2)
        self.TSGL.clicked.connect(self.onclick)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理员入口"))
        self.GLYRK.setText(_translate("Form", "管理员入口"))
        self.DZGL.setText(_translate("Form", "读者管理"))
        self.TSGL.setText(_translate("Form", "图书管理"))
        self.pushButton_3.setText(_translate("Form", "退出"))
    
    def onclick(self):
        self.newWindow=Ui_Bookma()
        self.newWindow.show()

    def onclick2(self):
        self.newWindow=Ui_Userma()
        self.newWindow.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    #app.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    mainMindow = Ui_Manager()
    mainMindow.show()
    sys.exit(app.exec_())