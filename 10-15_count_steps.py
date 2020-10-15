
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

while True:

    # fine the (pythagorean) magnitude of acceleration, scaled by g
    x, y, z = cpx.acceleration
    a2 = math.sqrt(x*x+y*y+z*z)/g
    t2 = time.monotonic()

    slope1 = (a1-a0)/(t1-t0)
    slope2 = (a2-a1)/(t2-t1)

    # this is the condition that we worked out in an Excel
    # sheet in class on 2020-10-13
    # A "peak" means the slope changes from positive to negative
    # if the magnitude of acceleration is above some certain
    # minimum value, "a_floor"
    if(
        slope1>0 and slope2<0
        and a1 > a_floor
        ):

        num_steps += 1
        print("peak: ",a0,a1,a2,slope1,slope2,num_steps)
        print(bin(num_steps))

    # update the acceleration and time measurements, ie, move the "window"
    # forward in time
    a0=a1
    a1=a2
    t0=t1
    t1=t2

    time.sleep(read_delay)
    
'''
0b101
peak:  0.649415 1.86088 0.826091 5.87934 -5.11896 6
0b110
peak:  0.826091 2.24884 0.783161 6.9376 -7.21566 7
0b111
peak:  0.783161 1.67729 0.957144 4.33928 -3.54533 8
0b1000
peak:  0.957144 1.99361 0.763969 5.03003 -6.08284 9
0b1001
peak:  0.763969 1.48539 1.11111 3.51781 -1.85153 10
0b1010
peak:  1.11111 1.81763 0.867752 3.44513 -4.67632 11
0b1011
peak:  0.867752 1.54978 1.21627 3.30996 -1.64986 12
0b1100
peak:  1.01723 1.52095 0.743234 2.49182 -3.82875 13
0b1101
peak:  0.743234 1.31935 0.863385 2.78277 -2.25562 14
0b1110
peak:  0.863385 1.41878 0.510919 2.7082 -4.38513 15
0b1111
peak:  0.510919 1.40001 0.694755 4.31481 -3.47201 16
'''
