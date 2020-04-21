import sys
import time
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5 import uic
from UITEST import Ui_MainWindow
import random


class App(QMainWindow,Ui_MainWindow):

    def __init__(self,*args,**kwargs):
        super(App,self).__init__(*args,**kwargs)
        uic.loadUi('UITEST.ui',self)

        ##Push Button
        self.pushButton.pressed.connect(self.starttime)

    def starttime(self):
        Num = random.randrange(10,100,2)
        self.lcdNumber.display(str(Num))




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    