# NodeMCU/micropython programming with Fedora 26

### Workstation Requirements
* Fedora 26
* packages installed (with dnf):
  * ampy
  * esptool
  * screen

I was pleasantly surprised that these packages were all you need and that they
were available in the fedora 26 repository.

### Flash the firmware
* Download the micropython firmware for the ESP8266 [here.](http://micropython.org/download#esp8266)
* then use the write_flash.sh script to put the firmware on the chip

### Start writing some python code on the NodeMCU
* use screen to get at the REPL that's running on the chip:
  * screen /dev/ttyUSB0 11500 or run the nodemcu_repl.sh script
* in the screen session, use CTRL-a k to get out

### Copy a script to the NodeMCU to be run automatically
* ampy -p /dev/ttyUSB0 put main.py
* of course, edit main.py to do what you want
* if there is a problem, use the repl to see a traceback.

### More information
* Ken W Alger wrote a [blog post](http://www.kenwalger.com/blog/iot/micropython-and-nodemcu-esp8266/)
about getting started with the NodeMCU and micropython
* [The Micropython Docs](http://docs.micropython.org/en/latest/pyboard/) are geared
toward the pyboard, but still useful
