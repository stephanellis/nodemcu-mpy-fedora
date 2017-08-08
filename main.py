

import time
import json
import machine
import network
from umqtt.simple import MQTTClient

p = machine.Pin(2, machine.Pin.OUT)
p.on()
p2 = machine.Pin(4, machine.Pin.PULL_UP)


BLINK_DELAY=0.1
MEASR_DELAY=10

def blink():
    p.off()
    time.sleep(BLINK_DELAY)
    p.on()
    p2.on()
    time.sleep(BLINK_DELAY)
    p2.off()

    

f = open("settings.json")
raw_settings = "".join(f.readlines())
f.close()

settings = json.loads(raw_settings)

sta = network.WLAN(network.STA_IF)
sta.active(True)
sta.connect(settings["network"], settings["password"])

c = MQTTClient(settings["name"], settings["broker"])

while True:
    if sta.isconnected():
        c.connect()
        break
    time.sleep(1)

while True:
    blink()
    c.publish(settings["topic"], "Blinked!")
    time.sleep(MEASR_DELAY)
