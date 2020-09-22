# This prints out acceleration and avoids divergence issue for vertical (ax=0) orientation
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython

import time
import math
from adafruit_circuitplayground.express import cpx

while True:
    x, y, z = cpx.acceleration
    print("vec(accel) = ",(x,y,z))
    time.sleep(0.5)

    if(abs(x)>0):
        angle_from_vertical = math.atan(y/x)
    else:
        angle_from_vertical = math.pi*0.5
        
    print("angle from vertical (deg) = ",
        angle_from_vertical *180/math.pi,
        "\n")
