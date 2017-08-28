import machine
import ssd1306

i2c = machine.I2C(scl=machine.Pin(14), sda=machine.Pin(12))
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.text("esp8266, it's verkink!", 0,0)
oled.show()
