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

# how long does the rise and fall of the sawtooth last?
period = 0.5 # seconds
# How many levels do you want?
num_levels = 10
# note, if period/num_levels is more than about 2.0s/40 = 50ms, the LED's flashes start to become visible.
# also, since the pattern is a sawtooth, there are actually 2*num_levels written out during one period
# thus, warning message
if((period/num_levels)>(2./40.)):
    print("use more levels, LED might have visible flashing")


# loop over the set of brightness levels that will be written out
# build a list with .append() function/method
i=0
levels=[]
while (i<num_levels):
    levels.append(1.0*i/num_levels)
    i = i+1
    print("levels are: ",levels)
while (i>0):
    levels.append(1.0*i/num_levels)
    i = i-1
    print("levels are: ",levels)

#print("length of levels",len(levels))
#print("period = ",period)
dt = period/len(levels)
#print("dt = ",dt)


# this implements the periodic sawtooth wave
while True:
    for brightness in levels:
        # brightness is measured out of a max of 1.0
        T_fast = dt
        T_on = brightness*T_fast
        T_off = (1-brightness)*T_fast
        led.value = True
        time.sleep(T_on)
        led.value = False
        time.sleep(T_off)
 
