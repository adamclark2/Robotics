#!/usr/bin/env python3 -S
# -S might make python3 faster on the ARM BRICK THING

# Find The Goal Simple
# By:
# Adam Clark <adam.clark2@maine.edu>
# Steven Doherty <steven.doherty@maine.edu>
#
# When started on a colored piece of paper
# it will find another piece of paper 

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from time import sleep
import time
from ev3dev2.sound import Sound

# Constants
C_NO_COLOR = 0
C_BLACK = 1
C_BLUE = 2
C_GREEN = 3
C_YELLOW = 4
C_RED = 5
C_WHITE = 6
C_BROWN = 7

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


initial_spot = cl.color()

hasFoundFinishGoal = False
RMC.on(100)
LMC.on(100)
while !hasFoundFinishGoal:
    if cl.color() != C_BLACK and cl.color() != C_NO_COLOR and cl.color() != C_WHITE and cl.color() != initial_spot:
        # Found the goal!
        hasFoundFinishGoal = True
        RMC.off()
        LMC.off()

    else if cl.color() == C_BLACK or cl.color() == C_NO_COLOR :
        # Turn & go
        RMC.on(-25)
        LMC.on(25)
        sleep(0.5)

    else if cl.color() == C_WHITE:
        RMC.on(100)
        LMC.on(100)

hasFoundFirstGoal = False
while !hasFoundFirstGoal:
        if cl.color() != C_BLACK and cl.color() != C_NO_COLOR and cl.color() != C_WHITE and cl.color() == initial_spot:
        # Found the goal!
        hasFoundFirstGoal = True
        RMC.off()
        LMC.off()

    else if cl.color() == C_BLACK or cl.color() == C_NO_COLOR :
        # Turn & go
        RMC.on(-25)
        LMC.on(25)
        sleep(0.5)

    else if cl.color() == C_WHITE:
        RMC.on(100)
        LMC.on(100)

# Done with Program
RMC.off()
LMC.off()