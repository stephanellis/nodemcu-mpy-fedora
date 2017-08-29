import machine
import time

r1 = machine.Pin(14, machine.Pin.OUT, value=1)
r2 = machine.Pin(12, machine.Pin.OUT, value=1)


while True:
    r1(0)
    r2(0)
    time.sleep(1)
    r1(1)
    r2(1)
    time.sleep(1)


