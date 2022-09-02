import sys
import PyQt5.QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

def clickFunc():
    print("yup_done")

def appWindow():
    appStart= QApplication(sys.argv)
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300)
    win.setWindowTitle("Hello Dc!")

    label1 =QtWidgets.QLabel(win)
    label1.setText("helo This is Divagar !")
    label1.move(50,50)

    button1 = QtWidgets.QPushButton(win)
    button1.setText("click")
    button1.move(100,100)
    button1.clicked.connect(clickFunc)


    win.show()
    sys.exit(appStart.exec_())
appWindow()

