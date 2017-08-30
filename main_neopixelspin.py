import machine
import neopixel
from urandom import getrandbits
import time

def rand():
    return int(getrandbits(8))

np = neopixel.NeoPixel(machine.Pin(12), 12)
while True:
    for i in range(12):
        np[i] = (0, 0, 2)
        np.write()
        time.sleep(.04)
        np[i] = (0, 0, 0)

