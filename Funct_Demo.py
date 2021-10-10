#!/usr/bin/env python2.7

# -*- coding: utf-8 -*-


#!/usr/bin/env python3
from time import sleep
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711

motor = 38
dout=36
sck=35
GPIO.cleanup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(motor,GPIO.OUT) #Motor high low


from PyQt5 import QtCore, QtGui, QtWidgets

from DEV1 import Feed_Now, Feed_Later, setTime

import sys
sys.path.append('/home/pi/.local/lib/python2.7/site-packages')


try:
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    hx = HX711(dout_pin=dout, pd_sck_pin=sck)
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    err = hx.zero()
    # check if successful
    if err:
        raise ValueError('Tare is unsuccessful.')

    reading = hx.get_raw_data_mean()
    if reading:  # always check if you get correct value or only False
        # now the value is close to 0
        print('Data subtracted by offset but still not converted to units:',
                reading)
    else:
        print('invalid data', reading)

    # In order to calculate the conversion ratio to some units, in my case I want grams,
    # you must have known weight.
    input('Put known weight on the scale and then press Enter')
    reading = hx.get_data_mean()
    if reading:
        print('Mean value from HX711 subtracted by offset:', reading)
        known_weight_grams = input(
            'Write how many grams it was and press Enter: ')
        try:
            value = float(known_weight_grams)
            print(value, 'grams')
        except ValueError:
            print('Expected integer or float and I have got:',
                    known_weight_grams)

        # set scale ratio for particular channel and gain which is
        # used to calculate the conversion to units. Required argument is only
        # scale ratio. Without arguments 'channel' and 'gain_A' it sets
        # the ratio for current channel and gain.
        ratio = reading / value  # calculate the ratio for channel A and gain 128
        hx.set_scale_ratio(ratio)  # set ratio for current channel
        print('Ratio is set.')
    else:
        raise ValueError(
            'Cannot calculate mean value. Try debug mode. Variable reading:', reading)

except (KeyboardInterrupt, SystemExit):
    print('Bye :)')

def read_weight():
    GPIO.setmode(GPIO.BOARD)
    sum=0
    # for i in range(10):
    #     sum = sum + hx.get_weight_mean(10)
    #     sleep(.1)
    
    ui.Check_Weight.setText(str(hx.get_weight_mean(10)))
    return

    
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
