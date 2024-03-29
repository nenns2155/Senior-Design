#!/usr/bin/env python3
import RPi.GPIO as GPIO  # import GPIO
from hx711 import HX711  # import the class HX711
import time

try:
    GPIO.setmode(GPIO.BCM)  # set GPIO pin mode to BCM numbering
    # Create an object hx which represents your real hx711 chip
    # Required input parameters are only 'dout_pin' and 'pd_sck_pin'
    hx = HX711(dout_pin=16, pd_sck_pin=19)
    # measure tare and save the value as offset for current channel
    # and gain selected. That means channel A and gain 128
    # err = hx.zero()
    # # check if successful
    # if err:
    #     raise ValueError('Tare is unsuccessful.')

    # reading = hx.get_raw_data_mean()
    # if reading:  # always check if you get correct value or only False
    #     # now the value is close to 0
    #     print('Data subtracted by offset but still not converted to units:',
    #           reading)
    # else:
    #     print('invalid data', reading)

    # # In order to calculate the conversion ratio to some units, in my case I want grams,
    # # you must have known weight.
    # input('Put known weight on the scale and then press Enter')
    # reading = hx.get_data_mean()
    # if reading:
    #     print('Mean value from HX711 subtracted by offset:', reading)
    #     known_weight_grams = input(
    #         'Write how many grams it was and press Enter: ')
    #     try:
    #         value = float(known_weight_grams)
    #         print(value, 'grams')
    #     except ValueError:
    #         print('Expected integer or float and I have got:',
    #               known_weight_grams)

    #     # set scale ratio for particular channel and gain which is
    #     # used to calculate the conversion to units. Required argument is only
    #     # scale ratio. Without arguments 'channel' and 'gain_A' it sets
    #     # the ratio for current channel and gain.
    #     ratio = reading / value  # calculate the ratio for channel A and gain 128
    #     hx.set_scale_ratio(ratio)  # set ratio for current channel
    #     print('Ratio is set.')
    # else:
    #     raise ValueError('Cannot calculate mean value. Try debug mode. Variable reading:', reading)

    # # Read data several times and return mean value
    # # subtracted by offset and converted by scale ratio to
    # # desired units. In my case in grams.
    # print("Now, I will read data in infinite loop. To exit press 'CTRL + C'")
    # input('Press Enter to begin reading')
    # print('Current weight on the scale in grams is: ')
    lastreading = hx._read()
    count = 0
    sum = 0
    while True:
        reading = hx._read()
        if reading == -1:
            lastreading = reading
            continue
        elif count == 10:
            print("Average of the last 10 readings:", sum/10 )
            count=0
            sum=0
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

finally:
    GPIO.cleanup()
