### DEV
def update_voltage():
        ##read in pin voltages.
        ui.Feed_Now.setText("update")

def TEST():
    import time
    import RPi.GPIO as GPIO

    pin = 36
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT) #Motor high low

    i=0
    while i<=10:
        GPIO.output(pin,1)
        time.sleep(.5)
        GPIO.output(pin,0)
        time.sleep(.5)
        i=i+1
    GPIO.cleanup()

def Feed_Now():
    import time
    import RPi.GPIO as GPIO

    pin = 36
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT) #Motor high low

    GPIO.output(pin,1)
    time.sleep(5)
    GPIO.output(pin,0)
    
    GPIO.cleanup()

def Feed_Later(Delay):
    import time
    import RPi.GPIO as GPIO

    pin = 36
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pin,GPIO.OUT) #Motor high low

    time.sleep(Delay)
    GPIO.output(pin,1)
    time.sleep(5)
    GPIO.output(pin,0)
        
    GPIO.cleanup()

if __name__ == "__main__":
    TEST()



# def motor(feedt):
#     starttime = time.time()
#     endtime = starttime + feedt

#     GPIO.output(32,True)

#     while True:
#         if time.time() < endtime:
#             GPIO.output(32,False)
#             return

#Test Test Test

# feedt = 1000 #Length of pulse (in ms) that the motor will run for feeding.

# motor(feedt)

#try:
#    while True:
#        if "the time to feed is now" == True:
#            motor(feedt)
#