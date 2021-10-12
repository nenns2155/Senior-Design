import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)

GPIO.output(38,1)
time.sleep(5)
GPIO.output(38,0)
    
GPIO.cleanup()