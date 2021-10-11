motor = 38

def TEST():
    import time
    #import RPi.GPIO as GPIO

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
    
    GPIO.output(motor,1)
    time.sleep(5)
    GPIO.output(motor,0)
    
    GPIO.cleanup()

def Feed_Later(Delay):
    import time
    import RPi.GPIO as GPIO

    time.sleep(Delay)
    GPIO.output(pin,1)
    time.sleep(5)
    GPIO.output(pin,0)
        
    GPIO.cleanup()

def setTime(jobString):
    import sys
    sys.path.append('/home/pi/.local/lib/python2.7/site-packages')
    from crontab import CronTab
    cron = CronTab(user = True)
    job = cron.new(command = jobString)
    d = input("Enter the day of the week to feed (0-6 starting with Sunday being 0):")
    h = input("Enter the hour to feed (0-23 starting with 0 at midnight):")
    minut = input("Enter the minute to feed (0-59):")
    job.minute.on(minut)
    job.hour.on(h)
    job.dow.every(d)
    
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
