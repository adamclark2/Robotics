#!/usr/bin/env python3

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep

print("Program Running...")

cl = ColorSensor() 
leds = Leds()
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)

def stopMotors():
    leds.all_off()
    RMC.off()
    LMC.off()

import atexit
atexit.register(stopMotors)

leds.all_off()

while True:
    light_intensity = cl.reflected_light_intensity
    if light_intensity > 20:
        # White Part of the Board 
        # This code attempts micro adjustments
        LMC.off()
        RMC.off()

        # Try to turn 
        if light_intensity > 20:
            LMC.on(-25)
            RMC.on(25)
            leds.all_off()
            leds.set_color('LEFT', 'GREEN')

            i = 0
            while light_intensity > 20 and i < 25:
                i = i + 1
                sleep(0.005)
                light_intensity = cl.reflected_light_intensity
                if light_intensity < 20:
                    LMC.off()
                    RMC.off()

            if light_intensity > 20:
                LMC.on(25)
                RMC.on(-25)
                leds.all_off()
                leds.set_color('RIGHT', 'GREEN')

                i = 0
                while light_intensity > 20 and i < 50:
                    i = i + 1
                    sleep(0.005)
                    light_intensity = cl.reflected_light_intensity
                    if light_intensity < 20:
                        LMC.off()
                        RMC.off()

        if light_intensity > 20:
            # This code attempts a bigger adjustment
            LMC.on(-25)
            RMC.on(25)
            i = 0
            while light_intensity > 20 and i < 100:
                i = i + 1
                sleep(0.005)
                light_intensity = cl.reflected_light_intensity
                if light_intensity < 20:
                    LMC.off()
                    RMC.off()

            if light_intensity > 20:
                LMC.on(25)
                RMC.on(-25)

                i = 0
                while light_intensity > 20 and i < 200:
                    i = i + 1
                    sleep(0.005)
                    light_intensity = cl.reflected_light_intensity
                    if light_intensity < 20:
                        LMC.off()
                        RMC.off()

        LMC.off()
        RMC.off()

    else:
        # Black Part of the Board 
        leds.all_off()

        RMC.on(100)
        LMC.on(100)