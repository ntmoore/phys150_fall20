# this example is from adafruit
# https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/neopixels

"""This example lights up the first NeoPixel red."""
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
cp.pixels.fill((50,50,50))
 
i=0;
while True:
    cp.pixels[0] = (255-i, i, 0)
    cp.pixels[1] = (0,255-i, i, )
    cp.pixels[2] = (255-i, 0,i, )
    i+=1
    if(i>255) :
        i=0
    time.sleep(0.01)
    
# how can this be modified to produce constant brightness? (normalize RGB values via pythagorus?)
# are the pixels uniform?

