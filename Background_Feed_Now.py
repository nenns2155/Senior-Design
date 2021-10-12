import time
import RPi.GPIO as GPIO
    
GPIO.output(motor,1)
time.sleep(5)
GPIO.output(motor,0)
    
GPIO.cleanup()