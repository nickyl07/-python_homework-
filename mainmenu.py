import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from managerUI import Ui_Form
from userUI import Ui_Read
import pymysql
import qdarkstyle
#主页
class Ui_first(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, first):
        first.setObjectName("first")
        first.resize(640, 550)
        self.DZ = QtWidgets.QPushButton(first)
        self.DZ.setGeometry(QtCore.QRect(260, 210, 93, 28))
        self.DZ.setObjectName("DZ")
        self.GLY = QtWidgets.QPushButton(first)
        self.GLY.setGeometry(QtCore.QRect(260, 270, 93, 28))
        self.GLY.setObjectName("GLY")
        self.exit = QtWidgets.QPushButton(first)
        self.exit.setGeometry(QtCore.QRect(260, 330, 93, 28))
        self.exit.setObjectName("exit")
        self.label = QtWidgets.QLabel(first)
        self.label.setGeometry(QtCore.QRect(190, 70, 269, 69))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(first)
        self.exit.clicked.connect(first.close)
        self.DZ.clicked.connect(self.onclick)
        self.GLY.clicked.connect(self.onclick2)
        QtCore.QMetaObject.connectSlotsByName(first)

    def retranslateUi(self, first):
        _translate = QtCore.QCoreApplication.translate
        first.setWindowTitle(_translate("first", "主页"))
        self.DZ.setText(_translate("first", "读者入口"))
        self.GLY.setText(_translate("first", "管理员入口"))
        self.exit.setText(_translate("first", "退出"))
        self.label.setText(_translate("first", "图书馆管理系统"))

    def onclick(self):
        self.newWindow=Ui_Read()
        self.newWindow.show()

    def onclick2(self):
        self.newWindow=Ui_Form()
        self.newWindow.show()

if __name__ == "__main__":
    App = QtWidgets.QApplication(sys.argv)
    App.setWindowIcon(QtGui.QIcon('F:/pythonpythonpython/python课/【数据库】图书管理系统/img/logo.png'))
    App.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())
    ex =Ui_first()
    ex.show()
    sys.exit(App.exec_())
