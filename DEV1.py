import time
import RPi.GPIO as GPIO

pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT) #Motor high low
#
#
#

### DEV
GPIO.output(pin,True)




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
#finally:

