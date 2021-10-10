#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-


#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import time

motor = 38
dout=36
sck=35
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor,GPIO.OUT) #Motor high low


from PyQt5 import QtCore, QtGui, QtWidgets

from DEV1 import Feed_Now, Feed_Later, setTime

import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')

def read_weight():
    try:
        hx = HX711(dout_pin=36, pd_sck_pin=35)

        lastreading = hx._read()
        count = 0
        sum = 0
        while True:
            reading = hx._read()
            if reading == -1:
                lastreading = reading
                continue
            elif count == 20:
                ui.Check_Weight.setText(str(sum/20))
                return
            elif reading < 0:
                lastreading = reading
                continue
            elif reading == False:
                lastreading = reading
                continue
            elif abs(lastreading/reading) > 1.25 or abs(lastreading/reading) < .75:
                lastreading = reading
                continue
            else:
                sum = sum + reading
                count = count + 1
                lastreading = reading
            time.sleep(.1)
    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')
        return

    finally:
        GPIO.cleanup()

    
#########################################################################
#########################################################################
    


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
        self.Feed_In_30.clicked.connect(lambda: Feed_Later(30))
        self.Check_Weight.clicked.connect(lambda: read_weight())


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

    # timer = QtCore.QTimer()
    # timer.timeout.connect()
    # timer.start(10000)

    sys.exit(app.exec_())
