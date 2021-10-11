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
            
            lastreading = reading    
            
    

    except (KeyboardInterrupt, SystemExit):
        print('Bye :)')

def Voltage_to_Weight(voltage):

    A = 190033
    B = 262378.645
    C = 256951.0917

    return (voltage - B)/A

def Calibration():

    import numpy as np

    weight = []
    voltage = []

    for i in range(0, 42, 2):
        i=i/4
        input("Press enter when {} lbs are on the scale.".format(i))
        weight.append(i)
        voltagepoint = Read_Voltage(20)
        voltage.append(voltagepoint)
        print("Weight equals:", i)
        print("Voltage equals:",voltagepoint)


    [A,B,C] = np.polyfit(weight, voltage, 2)

    print('A equals:', A)
    print('B equals:', B)
    print('C equals:', C)

if __name__ == "__main__":
    import RPi.GPIO as GPIO
    from hx711 import HX711
    import time

    # Calibration()
    while True:
        print(Read_Voltage(1))
    




