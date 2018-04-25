

import esp
import dht
import time
import json
import machine
import network
from umqtt.robust import MQTTClient


d = dht.DHT11(machine.Pin(2))
p2 = machine.Pin(4, machine.Pin.PULL_UP)

BLINK_DELAY=0.1
MEASR_DELAY=60

def blink():
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

#randomNum = int.from_bytes(uos.urandom(3), 'little')
#myMqttClient = bytes("client_"+str(randomNum), 'utf-8')

c = MQTTClient(
    client_id = "client_1",
    server = settings["broker"],
    user = settings["userid"],
    password = settings["mqttapikey"],
    port = 1883
    )

while True:
    print("connecting to wifi")
    if sta.isconnected():
        print("connected!")
        c.connect()
        print("mqtt connected!")
        break
    time.sleep(1)

counter = 0
while True:
    d.measure()
    blink()
    credentials = bytes("channels/{:s}/publish/{:s}".format(settings["channel"], settings["apikey"]), 'utf-8')
    payload = bytes("field1={:.1f}&field2={:d}&field3={:d}&field4={:d}\n".format(ctof(d.temperature()), get_rssi(), esp.freemem(), d.humidity()), 'utf-8')
    c.publish(credentials, payload)
    print("Blinked! Free mem: {}, Count: {}, Temp: {}, RH: {}, RSSI: {}".format(esp.freemem(), counter, ctof(d.temperature()), d.humidity(), get_rssi()))
    counter += 1
    time.sleep(MEASR_DELAY)
