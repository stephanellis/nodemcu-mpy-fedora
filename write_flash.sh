#! /bin/bash

esptool --port /dev/ttyUSB0 erase_flash

esptool --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 $1
