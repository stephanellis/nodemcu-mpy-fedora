#! /bin/bash

cp $1 main.py

ampy -p /dev/ttyUSB0 put main.py
ampy -p /dev/ttyUSB0 put settings.json
