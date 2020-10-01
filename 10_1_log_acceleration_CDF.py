#Adapted from
#https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/python-circuitpython
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out

import time
from adafruit_circuitplayground.express import cpx

def get_accel_on_button():
    x,y,z=cpx.acceleration
    current_time = time.monotonic()
    g=9.801
    if cpx.button_a:
        cpx.red_led = True
        time.sleep(0.05)
        fp.write('{0:f},{1:f},{2:f},{3:f}\n'.format(current_time,x/g,y/g,z/g))
        print('logging',(current_time,x/g,y/g,z/g))
        fp.flush()
    else:
        cpx.red_led = False
        time.sleep(0.05)
        print((current_time,x/g,y/g,z/g))
    return

#will try and see if a file is writeable, if it is it continues, if not it goes to the except statement
try:
    #open a file to save the data to
    with open("/acceleration.txt", "a") as fp:
        while True:
            get_accel_on_button()

# will flash the D13 red LED to let us know we can edit the code.py file (i.e. the storage is writeable)
except OSError as e:
    delay = 0.5
    if e.args[0] == 28:
        delay = 0.25
    while True:
        cpx.red_led = not cpx.red_led
        time.sleep(delay)
        get_accel_on_button()