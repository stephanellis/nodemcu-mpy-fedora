#
# example main.py for blinking
#

import esp
import time
import machine
import network


PIN_D0   = 16
PIN_D1   = 5
PIN_D2   = 4
PIN_D3   = 0
PIN_D4   = 2
PIN_D5   = 14
PIN_D6   = 12
PIN_D7   = 13
PIN_D8   = 15
PIN_D9   = 3
PIN_D10  = 1


p = machine.Pin(PIN_D4, machine.Pin.OUT)
p.on()


BLINK_DELAY=0.1
WAIT_DELAY=2

def blink():
    p.off()
    time.sleep(BLINK_DELAY)
    p.on()

while True:
    blink()
    time.sleep(WAIT_DELAY)
