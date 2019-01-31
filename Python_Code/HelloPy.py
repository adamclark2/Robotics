#!/usr/bin/env python

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank

# Documentation
# https://sites.google.com/site/ev3devpython/learn_ev3_python/using-motors

m = LargeMotor(OUTPUT_A)
m.on(speed=45)