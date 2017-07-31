

import time
import machine

DELAY=1

p = machine.Pin(2, machine.Pin.OUT)

while True:
    p.on()
    time.sleep(DELAY)
    p.off()
    time.sleep(DELAY)
    p.on()
