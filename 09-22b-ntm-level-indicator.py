# 
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython

import time
import math
from adafruit_circuitplayground.express import cpx
from adafruit_circuitplayground import cp
cp.pixels.brightness = 0.05


while True:
    
    # measure accel "num" times and compute an average
    sum_angle=0.0
    num=10
    i=0
    while (i<num):
        x, y, z = cpx.acceleration
        if(abs(x)>0):
            angle_from_vertical = math.atan(y/x)
        else:
            angle_from_vertical = math.pi*0.5
        sum_angle += angle_from_vertical *180/math.pi
        i+=1
    avg_angle = sum_angle/(1.0*num) # forcing float math
    
    # report results
    print("angle from vertical (deg) = ",
        avg_angle,
        "\tavg over ",num," measurements\n")

    time.sleep(0.5)
    
    # turn on neopixel LED based on the quality of level.
    if(abs(avg_angle)<1.0): 
        cp.pixels[2]=(0,50,0)
        cp.pixels[7]=(0,50,0)
    else: 
        cp.pixels[2]=(50,0,0)
        cp.pixels[7]=(50,0,0)

# you could certainly make this pattern better! 

"""
output:
angle from vertical (deg) =  -4.40966 	avg over  10  measurements

angle from vertical (deg) =  -4.45226 	avg over  10  measurements

angle from vertical (deg) =  -4.45013 	avg over  10  measurements

"""
