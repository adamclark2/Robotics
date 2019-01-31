#!/usr/bin/env python3

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

print("Program Running...")

cl = ColorSensor() 
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)

def stopMotors():
    RMC.off()
    LMC.off()

import atexit
atexit.register(stopMotors)

while True:
    if cl.reflected_light_intensity > 20:
        # White Part
        LMC.off()

        # Try to turn 
        if cl.reflected_light_intensity > 20:
            LMC.on_for_degrees(speed=25, degrees=(-360*4), brake=True, block=False)
            RMC.on_for_degrees(speed=25, degrees=(360*4), brake=True, block=False)

            for i in range(0,200):
                if cl.reflected_light_intensity < 20:
                    LMC.off()
                    RMC.off()

        if cl.reflected_light_intensity > 20:
            LMC.on_for_degrees(speed=25, degrees=(360*4), brake=True, block=False)
            RMC.on_for_degrees(speed=25, degrees=(-360*4), brake=True, block=True)
            LMC.on_for_degrees(speed=25, degrees=(360*4), brake=True, block=False)
            RMC.on_for_degrees(speed=25, degrees=(-360*4), brake=True, block=False)

            for i in range(0,200):
                if cl.reflected_light_intensity < 20:
                    LMC.off()
                    RMC.off()

        LMC.off()
        RMC.off()

    else:
        # Black
        RMC.on(100)
        LMC.on(100)