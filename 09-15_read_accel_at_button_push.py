""" 
When button A is pushed, the system prints out 3d acceleration
Units of accel are m/s^2, note, "down" is 9.8m/s^2 

related example
https://learn.adafruit.com/make-it-shake-rattle-and-roll?view=all
"""
from adafruit_circuitplayground import cp
from adafruit_circuitplayground.express import cpx
import time

state=0
t0=time.monotonic()
g=9.8
while True:
    time.sleep(0.1)
    if cp.button_a:
        x, y, z = cpx.acceleration        
        print(x,y,z, "\t",x/g,y/g,z/g)
        
"""
code.py output:
0.0 -0.306437 9.46126 	 0.0 -0.0312691 0.965435
0.0383047 -0.191523 9.49956 	 0.00390864 -0.0195432 0.969343
0.0 -0.153219 9.38465 	 0.0 -0.0156346 0.957617
0.0 -0.268133 9.30804 	 0.0 -0.0273605 0.9498
"""
