# Nathan Moore
# Create a sawtooth snoring function
# https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code
#
import board
import digitalio
import time

# set up the (red) LED
led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

# how long dows the rise and fall of the sawtooth last?
period = 0.5
# How many levels do you want?
num_levels = 10
#levels go from 0 to num_levels
levels = range(0,num_levels,1)
print("levels are: ",levels)
levels = levels/num_levels
print("levels are: ",levels)




while True:
    for brightness in levels:
        # brightness is measured out of a max of 1.0
        T_fast = 0.01
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        num_repeats=100
        i=0
        while (i<num_repeats):
            led.value = True
            time.sleep(T_on)
            led.value = False
            time.sleep(T_off)
            i=i+1
