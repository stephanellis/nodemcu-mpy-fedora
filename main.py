

import time
import machine

DELAY=1

p = machine.Pin(2, machine.Pin.OUT)

while True:
    print("LED off...")
    p.on()
    time.sleep(DELAY)
    print("LED on...")
    p.off()
    time.sleep(DELAY)
    p.on()
