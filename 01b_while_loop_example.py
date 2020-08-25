# from adafruit
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

while True:
    # this loop follows the same repetition as in the previous foreach example
    # the diffrerence is the while (instead of foreach) loop structure
    i=1
    while(i<6):
        print("Hello, CircuitPython!")
        led.value = True
        time.sleep(i/10)
        led.value = False
        time.sleep(i/10)
        # this is called a "counter" or "index" variable
        i = i+1
