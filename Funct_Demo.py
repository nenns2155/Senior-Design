#!/usr/bin/env python3

import RPi.GPIO as GPIO  # import GPIO
import sys
import time
import numpy as np

from hx711 import HX711  # import the class HX711
from PyQt5 import QtCore, QtGui, QtWidgets

from Weight import Calibration, Read_Voltage, Voltage_to_Weight
from DEV1 import Feed_Now, Feed_Later, setTime




motor = 38
dout=36 #16
sck=35 #19
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor,GPIO.OUT) #Motor high low
GPIO.setup(32, GPIO.OUT)
GPIO.output(32,1)

sys.path.append('/home/pi/.local/lib/python2.7/site-packages')

############################
##Begin Program Definitions:
############################

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 320)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.Feed_Now = QtWidgets.QPushButton(self.centralwidget)
        self.Feed_Now.setGeometry(QtCore.QRect(60, 40, 131, 81))
        self.Feed_Now.setObjectName("Feed_Now")

        self.Feed_In_30 = QtWidgets.QPushButton(self.centralwidget)
        self.Feed_In_30.setGeometry(QtCore.QRect(250, 40, 131, 81))
        self.Feed_In_30.setObjectName("Feed_In_30")

        self.Check_Weight = QtWidgets.QPushButton(self.centralwidget)
        self.Check_Weight.setGeometry(QtCore.QRect(80, 160, 301, 51))
        self.Check_Weight.setObjectName("Check_Weight")

        self.Calibration = QtWidgets.QPushButton(self.centralwidget)
        self.Calibration.setGeometry(QtCore.QRect(400 ,160, 50, 50))
        self.Calibration.setObjectName("Calibration")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 480, 26))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        ##Implementing Buttons
        self.Feed_Now.clicked.connect(lambda: Feed_Now())
        self.Feed_In_30.clicked.connect(lambda: setTime())
        self.Check_Weight.clicked.connect(lambda: self.Check_Weight.setText(Read_Voltage(1)))
        self.Calibration.clicked.connect(lambda: Calibration())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Feed_Now.setText(_translate("MainWindow", "Feed Now"))
        self.Feed_In_30.setText(_translate("MainWindow", "Feed In 30 Seconds"))
        self.Check_Weight.setText(_translate("MainWindow", "Check Weight"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())
