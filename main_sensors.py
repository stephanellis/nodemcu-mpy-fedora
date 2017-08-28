

import esp
import dht
import time
import json
import machine
import network
from umqtt.simple import MQTTClient

p = machine.Pin(2, machine.Pin.OUT)
p.on()
p2 = machine.Pin(4, machine.Pin.PULL_UP)

d = dht.DHT11(machine.Pin(2))

BLINK_DELAY=0.1
MEASR_DELAY=2

def blink():
    p.off()
    time.sleep(BLINK_DELAY)
    p.on()
    p2.on()
    time.sleep(BLINK_DELAY)
    p2.off()


def get_rssi():
    nets = sta.scan()
    for n in nets:
        if n[0].decode() == settings["network"]:
            return n[3]
    return None

def ctof(t):
    return t * (9 / 5) + 32

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

counter = 0
while True:
    d.measure()
    blink()
    c.publish(settings["topic"], "Blinked! Free mem: {}, Count: {}, Temp: {}, RH: {}, RSSI: {}".format(esp.freemem(), counter, ctof(d.temperature()), d.humidity(), get_rssi()))
    counter += 1
    time.sleep(MEASR_DELAY)
