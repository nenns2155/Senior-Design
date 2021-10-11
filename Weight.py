##Imports???

def Read_Voltage(samples):
    try:
        GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
        hx = HX711(dout_pin=16, pd_sck_pin=19)

        lastreading = hx._read()
        count = 0
        sum = 0
        while True:
            reading = hx._read()
            print(reading)
            if reading == -1:
                lastreading = reading
                pass
            elif count == samples:
                return Voltage_to_Weight(sum/samples)
            elif reading < 0:
                pass
            elif reading == False:
                pass
            elif abs(lastreading/reading) > 1.25 or abs(lastreading/reading) < .75:
                pass
            else:
                sum = sum + reading
                count = count + 1
                print(count)
            
            lastreading = reading    
            
    

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

def Voltage_to_Weight(voltage):

    A = -608.587
    B = 194733.675
    C = 256951.0917

    return A*voltage**2 + B*voltage + C

def Calibration():

    import numpy as np

    weight = []
    voltage = []

    for i in range(0, 42, 2):
        i=i/4
        input("Press enter when {} lbs are on the scale.".format(i))
        weight.append(i)
        voltage.append(Read_Voltage(20))


    [A,B,C] = np.polyfit(weight, voltage, 2)

    print('A equals:', A)
    print('B equals:', B)
    print('C equals:', C)

if __name__ == "__main__":
    import RPi.GPIO as GPIO
    from hx711 import HX711
    import time
    while True:
        print(Read_Voltage())
    




