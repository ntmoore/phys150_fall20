# Carl Ferkinhoff
# starting from from adafruit example
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import time
from adafruit_circuitplayground import cp

# set up the (red) LED
#cp.pixels.brightness = 0.1
#cp.pixels.fill((50,50,50))
 

while True:
    #length = 255 #sets the length of the snore
    length = 360 # duration in seconds?
    j=0
    wait_down = .001
    wait_up = .001
    while (j<length):
        cp.pixels.fill((255-j, 0, 0))
        j = j+1
        time.sleep(wait_down)
    time.sleep(1)
    while (j>0):
        cp.pixels.fill((255-j, 0, 0))
        j = j-1
        time.sleep(wait_up)
