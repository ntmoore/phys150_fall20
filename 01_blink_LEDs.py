# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    print("Hello, CircuitPython!")
    led.value = True
    time.sleep(2)
    led.value = False
    time.sleep(1)
    
# Tasks:
# - Try an on-off cycle of 2:1, 0.2:0.1, 0.002:0.001 etc
# what is the shortest on-off cycle you can still see (seizure risk)
# Code SOS in Morse
# The LED's are indexed .... Create a chase pattern

# loops? Blink out an SOS pattern with a foreach loop that specifies duration
