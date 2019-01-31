#!/usr/bin/env python3

import os
os.system('setfont Lat15-TerminusBold14')

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

# https://sites.google.com/site/ev3devpython/learn_ev3_python/screen
print('This should be on ev3\'s screen')

cl = ColorSensor() 

# https://sites.google.com/site/ev3devpython/learn_ev3_python/using-sensors
while True:
    print(cl.reflected_light_intensity)
    sleep(1)