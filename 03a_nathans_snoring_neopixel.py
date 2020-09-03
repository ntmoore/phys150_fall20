# this code builds of the adafruit neopixel examples and the snoring code
# Nathan Moore

import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.05
cp.pixels.fill((50,50,50))

#writing out a "snoring" sawtooth pattern on a single neopixel

# how long does the rise and fall of the sawtooth last?
period = 1.0 # seconds
# How many levels do you want?
num_levels = 10

# loop over the set of brightness levels that will be written out
# build a list with .append() function/method
i=0
levels=[]
while (i<num_levels):
    levels.append(255*i/num_levels)
    i = i+1
    print("levels are: ",levels)
while (i>0):
    levels.append(255*i/num_levels)
    i = i-1
    print("levels are: ",levels)

print("length of levels",len(levels))
print("period = ",period)
dt = period/len(levels)
print("dt = ",dt)


# this implements the periodic sawtooth wave via a "foreach" loop iterating
# over the values in levels
while True:
    for brightness in levels:
        # brightness is measured out of a max of 255
        cp.pixels[0]=(int(brightness),0,0)
        time.sleep(period/(2*num_levels))
        

"""
code.py output:
levels are:  [0.0]
levels are:  [0.0, 25.5]
levels are:  [0.0, 25.5, 51.0]
levels are:  [0.0, 25.5, 51.0, 76.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0, 127.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0, 127.5, 102.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0, 127.5, 102.0, 76.5]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0, 127.5, 102.0, 76.5, 51.0]
levels are:  [0.0, 25.5, 51.0, 76.5, 102.0, 127.5, 153.0, 178.5, 204.0, 229.5, 255.0, 229.5, 204.0, 178.5, 153.0, 127.5, 102.0, 76.5, 51.0, 25.5]
length of levels 20
period =  1.0
dt =  0.05
"""
