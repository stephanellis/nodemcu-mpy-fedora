import machine
import ssd1306
import time
import dht

d = dht.DHT11(machine.Pin(13))

i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

def ctof(t):
    return t * (9 / 5) + 32

def display(temp, rh, c):
    oled.fill(0)
    oled.text("DHT 11 Sensor", 0,0)
    oled.text("Tmp: {} F".format(temp), 0, 16)
    oled.text("RH : {}%".format(rh), 0, 32)
    oled.text("Count: {}".format(c), 0, 48)
    oled.show()


c = 0
while True:
    c += 1
    d.measure()
    display(ctof(d.temperature()), d.humidity(), c)
    time.sleep(1)

