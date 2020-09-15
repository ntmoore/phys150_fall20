""" implementing a fairly simple stopwatch that's triggered by 
push of button A.  Stopwatch gives delay since last push

related documentation: https://circuitpython.readthedocs.io/en/5.3.x/shared-bindings/time/__init__.html
"""

from adafruit_circuitplayground import cp
import time

state=0
t0=time.monotonic()
while True:
    time.sleep(0.1)
    if cp.button_a:
        t1 = time.monotonic()
        dt = t1-t0
        t0=t1
        print("elapsed time is",dt," seconds")
        
"""
Note that this code is unstable for small values of bounce delay in line 11
code below comes from time.sleep(0.01)

Auto-reload is on. Simply save files over USB to run them or enter REPL to disable.
code.py output:
elapsed time is 1.61002  seconds
elapsed time is 0.0109863  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds

elapsed time is 2.85001  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0110168  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds

elapsed time is 8.64001  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0110168  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0110168  seconds
elapsed time is 0.0109863  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.0100098  seconds
elapsed time is 0.00997925  seconds
elapsed time is 0.0100098  seconds
"""
