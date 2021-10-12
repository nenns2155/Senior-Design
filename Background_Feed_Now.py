import time
import RPi.GPIO as GPIO
    
GPIO.setmode(GPIO.BOARD)
GPIO.setup(38,GPIO.OUT)

GPIO.output(motor,1)
time.sleep(5)
GPIO.output(motor,0)
    
GPIO.cleanup()