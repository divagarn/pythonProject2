import sys
import PyQt5.QtWidgets
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtGui import QIcon

def allInOneWin(QMainWindow):
    def __init__(self):
        super(allInOneWin, self).__init__()


def clickFunc():
    print("yup_done") #this is the functiom for the button when clicked

def appWindow():
    appStart= QApplication(sys.argv) #this is to start the gui application
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) #this is used to set the geometry or posisition
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

