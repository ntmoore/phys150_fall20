# this is not perfect
# Nathan Moore

import time
import math
from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
cp.pixels[2]=(0,50,0)
cp.pixels[7]=(0,50,0)

num_steps = 0

read_delay = 0.2 # how often do we sample acceleration? 0.2 seems good.

g=9.801
a_floor = 1.2   # this is the floor that's used in the peak-finiding method

# setup
x, y, z = cpx.acceleration
a0 = math.sqrt(x*x+y*y+z*z)/g
t0 = time.monotonic()

x, y, z = cpx.acceleration
a1 = math.sqrt(x*x+y*y+z*z)/g
t1 = time.monotonic()

x, y, z = cpx.acceleration
a2 = math.sqrt(x*x+y*y+z*z)/g
t2 = time.monotonic()

while True:

    # fine the (pythagorean) magnitude of acceleration, scaled by g
    x, y, z = cpx.acceleration
    a3 = math.sqrt(x*x+y*y+z*z)/g
    t3 = time.monotonic()

    slope1 = (a1-a0)/(t1-t0)
    slope2 = (a3-a2)/(t3-t2)
    
    # this is the condition that we worked out in an Excel
    # sheet in class on 2020-10-13
    # A "peak" means the slope changes from positive to negative
    # if the magnitude of acceleration is above some certain 
    # minimum value, "a_floor"
    if(
        slope1>0 and slope2<0 
        and (a1+a2)*0.5 > a_floor 
        ):
        
        num_steps += 1
        print("peak: ",a0,a1,a2,a3,slope1,slope2,num_steps)
        print(bin(num_steps))
       
    # update the acceleration and time measurements, ie, move the "window"
    # forward in time
    a0=a1
    a1=a2
    a2=a3
    t0=t1
    t1=t2
    t2=t3
    
    time.sleep(read_delay)
