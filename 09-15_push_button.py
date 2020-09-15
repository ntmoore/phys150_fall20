""" Starting from an adafruit example:
https://learn.adafruit.com/circuitpython-made-easy-on-circuit-playground-express/buttons
This example turns on the little red LED when button A 
is pressed."""
from adafruit_circuitplayground import cp
import time

state=0
while True:
    time.sleep(0.1)
    if cp.button_a:
        if(state==0):
            state = 1
            cp.red_led = True
        else:
            state = 0
            cp.red_led = False

        print("Button A pressed!")
