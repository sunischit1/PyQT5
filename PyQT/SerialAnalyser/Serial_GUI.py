import sys
import time
from PyQt5.QtGui import*
from PyQt5.QtCore import*
from PyQt5.QtWidgets import*
from PyQt5 import uic
from SerialAnalyser import Ui_MainWindow
import serial
import asyncio
#####################################################
class Worker(QThread):
    sinout=  pyqtSignal(str)
    def __init__(self, parent = None):
        super(Worker,self).__init__(parent)
        self.working = True

    def __del__(self):
        self.working = False
        self.wait()

    def run(self):
        global sr
        sr = serial.Serial('/dev/ttyUSB0',115200)
        while self.working == True:

            global x
            x = sr.readline()
            # Transmitting signal
            self.sinout.emit(str(x))

#####################################################
class App(QMainWindow,Ui_MainWindow):

    def __init__(self):
        super(App,self).__init__()
        uic.loadUi('SerialAnalyser.ui',self)
        self.thread = Worker()

        ##Push Button
        self.pushButton.pressed.connect(self.start)
        self.pushButton_2.pressed.connect(self.stop)
        self.thread.sinout.connect(self.showmsg)
      
    def start(self):
        self.pushButton.setEnabled(True)
        self.thread.start()
               
    def showmsg(self,x):
        self.plainTextEdit.setEnabled(True)
        self.plainTextEdit.appendPlainText(str(x))
    
    def stop(self):
        sr.close()
        self.thread.exit()
        
################################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
    