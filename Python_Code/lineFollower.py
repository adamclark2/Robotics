#!/usr/bin/env python3

# Line Follower
# By:
# Adam Clark <adam.clark2@maine.edu>
# Steven Doherty <steven.doherty@maine.edu>
#
# Program follows a line & beeps when the robot reaches the
# end or gets lost. Robot may turn around and navigate to the
# beginning. 

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
from ev3dev2.sound import Sound

print("Program Running...")

cl = ColorSensor() 
leds = Leds()
sound = Sound()
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)
leds.all_off()

def stopMotors():
    leds.all_off()
    RMC.off()
    LMC.off()

import atexit
atexit.register(stopMotors)

# Stop the motors if the light intensity is valid
# ticks is the amount of 5 miliseconds to run the loop
# led name is 'RIGHT' or 'LEFT' it turns the keypad led's on or off (For dramatic effect)
def doTurn(rightSpeed,leftSpeed,ticks,led_name):
    light_intensity = cl.reflected_light_intensity
    if light_intensity > 20:
        leds.all_off()
        leds.set_color(led_name, 'GREEN')
        RMC.on(rightSpeed)
        LMC.on(leftSpeed)
        i = 0
        while light_intensity > 20 and i < ticks:
            i = i + 1
            sleep(0.005)
            light_intensity = cl.reflected_light_intensity
            if light_intensity < 20:
                LMC.off()
                RMC.off()
                leds.all_off()

while True:
    light_intensity = cl.reflected_light_intensity
    if light_intensity > 20:
        # White Part of the Board 
        LMC.off()
        RMC.off()

        # This code attempts micro adjustments
        doTurn(25,-25,25,'LEFT')
        doTurn(-25,25,50,'RIGHT')

        # Try a bigger adjustment if the micro didn't work
        doTurn(25,-25,100,'LEFT')
        doTurn(-25,25,200,'RIGHT')

        LMC.off()
        RMC.off()

        # End of course or lost
        light_intensity = cl.reflected_light_intensity
        if light_intensity > 20:
            sound.tone(  [  (1000, 100, 0),  (1000, 100, 0),  (100, 100, 0),  (100, 100, 0)  ]  )

    else:
        # Black Part of the Board 
        leds.all_off()

        RMC.on(100)
        LMC.on(100)