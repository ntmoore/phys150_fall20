# this is a basic exampe from adafruit that spits ax, ay, az to serial
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython

import time
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print((x,y,z))
    time.sleep(0.5)
    
# Activities:
# 1. in Mu, turn on the plotter
# 2. Rotate the board and watch the three values. What does +/- number mean?
# 3. hold agains your stomach and breathe slowly.  Can you count your breaths from the data?
#
