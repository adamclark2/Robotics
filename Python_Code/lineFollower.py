#!/usr/bin/env python3

import os
os.system('setfont Lat15-TerminusBold14')

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from time import sleep

print("Program Running...")

cl = ColorSensor() 
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)

while True:
    if cl.reflected_light_intensity > 20:
        # White Part
        LMC.off()
        while cl.reflected_light_intensity > 20:
            RMC.on_for_degrees(speed=25, degrees=12, brake=True, block=False)

        RMC.off()

    else:
        # Black
        RMC.on(100)
        LMC.on(100)