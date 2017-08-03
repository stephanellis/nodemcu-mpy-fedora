

import time
import json
import machine
import network

p = machine.Pin(2, machine.Pin.OUT)
p.on()
BLINK_DELAY=0.1
MEASR_DELAY=10

def blink():
    p.off()
    time.sleep(BLINK_DELAY)
    p.on()
    

f = open("settings.json")
raw_settings = "".join(f.readlines())
f.close()

settings = json.loads(raw_settings)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(settings["network"], settings["password"])

while True:
    blink()
    time.sleep(MEASR_DELAY)
