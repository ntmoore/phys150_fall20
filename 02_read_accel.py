# this is a basic exampe from adafruit that spits ax, ay, az to serial
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython

import time
import math
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print((x,y,z))
    time.sleep(0.5)

    # compute the x/y angle from vertical
    angle_from_vertical = math.atan(y/x)
    print((angle_from_vertical ,angle_from_vertical *180/math.pi))
    
# Activities:
# 1. in Mu, turn on the plotter
# 2. Rotate the board and watch the three values. What does +/- number mean?
# 3. Raise the board quickly.  What happens to the three values?
# 4. hold agains your stomach and breathe slowly.  Can you count your breaths from the data?
# 5. How could you make a bike taillight that automatically gets brighter when you slow down?
# 
