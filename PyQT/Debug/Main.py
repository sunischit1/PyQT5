# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SerialDebug.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore,QtWidgets
from PyQt5.QtWidgets import QTableWidget,QTableWidgetItem,QGridLayout
from PyQt5.QtCore import QThread
import serial
import serial.tools.list_ports


 ####################### QTable Widget ##################

def GlobalVar_Table(self):
    self.GlobalVar_tabwidget.setHorizontalHeaderLabels(['variable','value'])
    self.GlobalVar_tabwidget.setItem(0,0,QTableWidgetItem("hello"))
    self.GlobalVar_tabwidget.setItem(0,1,QTableWidgetItem("hello"))

def LocalVar_Table(self):
    self.LocalVar_TabWidget.setHorizontalHeaderLabels(['variable','value'])
    self.LocalVar_TabWidget.setItem(0,0,QTableWidgetItem("local"))


############### Combo Box Logic ##################### 
def ComboBox_logic(self):
        self.comboBox.addItem("")
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            self.comboBox.addItem(str(p)[0:12])
############## Main window ########################
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(871, 573)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout_7.addWidget(self.label, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_7, 0, 0, 1, 1)
        self.gridLayout_10 = QtWidgets.QGridLayout()
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout_10.addWidget(self.label_4, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_10, 0, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.gridLayout.addWidget(self.plainTextEdit, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout, 1, 0, 6, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_2, 1, 1, 2, 1)
        self.gridLayout_5 = QtWidgets.QGridLayout()
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_5.addWidget(self.pushButton, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_5, 1, 2, 1, 1)
        self.gridLayout_6 = QtWidgets.QGridLayout()
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_6.addWidget(self.pushButton_2, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_6, 2, 2, 1, 1)
        self.gridLayout_8 = QtWidgets.QGridLayout()
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout_8.addWidget(self.label_2, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_8, 3, 1, 1, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.GlobalVar_tabwidget = QtWidgets.QTableWidget(self.centralwidget)
        self.GlobalVar_tabwidget.setRowCount(10)
        self.GlobalVar_tabwidget.setColumnCount(2)
        self.GlobalVar_tabwidget.setObjectName("GlobalVar_tabwidget")
        self.gridLayout_3.addWidget(self.GlobalVar_tabwidget, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_3, 4, 1, 1, 2)
        self.gridLayout_9 = QtWidgets.QGridLayout()
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_9, 5, 1, 1, 2)
        self.gridLayout_4 = QtWidgets.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.LocalVar_TabWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.LocalVar_TabWidget.setRowCount(10)
        self.LocalVar_TabWidget.setColumnCount(2)
        self.LocalVar_TabWidget.setObjectName("LocalVar_TabWidget")
        self.gridLayout_4.addWidget(self.LocalVar_TabWidget, 0, 0, 1, 1)
        self.gridLayout_12.addLayout(self.gridLayout_4, 6, 1, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 871, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        ## Combo Box Logic
        ComboBox_logic(self)

        ## Global Var Table widget
        GlobalVar_Table(self)

        ## Local Var Table widget
        LocalVar_Table(self)

        ## Functional Logic Block to Connect when button pressed
        self.pushButton.pressed.connect(self.Connect_Serial)

        ## Functional Logic Block to DisConnect when button is pressed
        self.pushButton_2.pressed.connect(self.Disconnect_Serial)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Debug Logs"))
        self.label_4.setText(_translate("MainWindow", "COM PORT"))
        self.pushButton.setText(_translate("MainWindow", "OPEN"))
        self.pushButton_2.setText(_translate("MainWindow", "CLOSE"))
        self.label_2.setText(_translate("MainWindow", "Global Variable"))
        self.label_3.setText(_translate("MainWindow", "Local Variable"))

    ###################### Connect Serial Port##############
    def Connect_Serial(self):
        global input_string
        global connection_status
        global selected_usb

        selected_usb = self.comboBox.currentText()

        print(selected_usb)

        connection_status = serial.Serial(selected_usb,115200)

        input_string = connection_status.readline()

        self.plainTextEdit.appendPlainText(str(input_string))
        
        print(input_string)

    ################ Disconnect Serial Port ################
    def Disconnect_Serial(self):
        connection_status.close()
    
   


    

######################################################################################
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

