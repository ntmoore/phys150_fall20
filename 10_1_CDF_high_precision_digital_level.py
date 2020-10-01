#Adapted from
#https://learn.adafruit.com/adafruit-lis3dh-triple-axis-accelerometer-breakout/python-circuitpython
#https://learn.adafruit.com/circuitpython-essentials/circuitpython-digital-in-out
# https://learn.adafruit.com/make-it-shake-rattle-and-roll/use-in-circuitpython


import time
import math
import board
import digitalio
import busio
import adafruit_lis3dh
import microcontroller
import neopixel


pixels = neopixel.NeoPixel(board.NEOPIXEL, 10, brightness=0.5, auto_write=False)

i2c = busio.I2C(board.ACCELEROMETER_SCL, board.ACCELEROMETER_SDA)
int1 = digitalio.DigitalInOut(board.ACCELEROMETER_INTERRUPT)  # Set this to the correct pin for the interrupt!
lis3dh = adafruit_lis3dh.LIS3DH_I2C(i2c, address=0x19,int1=int1)
lis3dh.range = adafruit_lis3dh.RANGE_2_G

led = digitalio.DigitalInOut(board.D13)
led.direction = digitalio.Direction.OUTPUT

num_average = 20 #the number of measurements to average together

pixels_hor = [5,6,7,8,9]
pixels_hor_range = [-20,-10,0,10,20]
half_lighting_arc_length = 12


#will try and see if a file is writeable, if it is it continues, if not it goes to the except statement
while True:
    x,y,z=0,0,0
    for measurement in range(0,num_average,1):
        #will loop and make measurements from the accelerometer for the num_average
        # Read accelerometer values (in m / s ^ 2).  Returns a 3-tuple of x, y, z
        # Divide them by 9.806 to convert to Gs. and adds the new measurements to the previous ones

        x = x + lis3dh.acceleration[0]/ adafruit_lis3dh.STANDARD_GRAVITY
        y = y + lis3dh.acceleration[1]/ adafruit_lis3dh.STANDARD_GRAVITY
        z = z + lis3dh.acceleration[2]/ adafruit_lis3dh.STANDARD_GRAVITY
    # Then divides by the num_average to get the average measurements
    x,y,z = (x/num_average,y/num_average,z/num_average)
    #angle = math.asin(y)*180/math.pi
    #computers the angle
    if abs(x) > 0:
        angle = math.atan(y/x)*180./math.pi
    else:
        angle = 90.0
    #print((angle,))


    for pixel in pixels_hor:
        delta_angle=pixels_hor_range[pixel-5]-angle
        if abs(delta_angle) >= half_lighting_arc_length:
            level = 0
        else:
            normalized_nearness = (1 - abs(delta_angle) / half_lighting_arc_length)
            level = int(normalized_nearness*50)
        print(level,angle)
        pixels[pixel] = (level, level, level)
    #pixels.brightness = (1-(.95*abs(angle)/90))**5
        if abs(angle)< .2 and pixel==7:
            pixels[7]=(level*3,0,0)
    pixels.show()