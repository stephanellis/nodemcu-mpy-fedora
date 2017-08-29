import machine
import ssd1306

# make the pins D5 and D5 into I2C bus
i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
# setup the ssd1306 display on that bus
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

# you can fit 6 Lines of text
# each with 16 characters
# the yellow area is 16 pixels tall
# the rest is in the blue area
oled.text("esp8266 number 2", 0,0)
oled.text(" It's verkink!--", 0, 16)
oled.text(">Sensor Output--", 0, 26)
oled.text(" Relay Control--", 0, 36)
oled.text(" Relay Control--", 0, 46)
oled.text(" Relay Control--", 0, 56)
oled.show()
