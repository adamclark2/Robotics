#!/usr/bin/python3

# Find The Goal
# By:
# Adam Clark <adam.clark2@maine.edu>
#
# When started on a colored piece of paper
# it will find another piece of paper &
# return to its original paper
# It will try to avoid books

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import UltrasonicSensor
from time import sleep
import time
from ev3dev2.sound import Sound
import random

# Constants
C_NO_COLOR = 0
C_BLACK = 1
C_BLUE = 2
C_GREEN = 3
C_YELLOW = 4
C_RED = 5
C_WHITE = 6
C_BROWN = 7

random.seed(100)

HOME = C_RED
GOAL = C_BLUE

print("Program Running...")

# Sensor Constructors
cl = ColorSensor() 
leds = Leds()
sound = Sound()
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)
us = UltrasonicSensor()

# Function Defs
def stopMotors():
    leds.all_off()
    RMC.off()
    LMC.off()

import atexit
atexit.register(stopMotors)

def nagHumans():
    i = 5
    while i >= 0:
        #if i % 3 == 0 or i % 5 == 0:
            # sound.tone(  [  (1000, 100, 0),  (1000, 100, 0),  (100, 100, 0),  (100, 100, 0)  ]  )

        leds.set_color('RIGHT', 'GREEN')
        leds.set_color('LEFT', 'GREEN')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        i = i - 1
    
    leds.all_off()

def backUpThenTurn():
    RMC.on(25)
    LMC.on(25)
    sleep(0.15)
    RMC.on(-25)
    LMC.on(25)
    sleep(random.random())

# Table is detected as yellow/brown
# Line may be detected as black, no color, or green ... idk why green
def isOnBlackLineOrTable(currentColor):
    return currentColor == C_BLACK or currentColor == C_NO_COLOR or currentColor == C_GREEN or currentColor == C_YELLOW or currentColor == C_BROWN

def hasBumpedBook():
    # Check to see if book is bumped
    return us.distance_centimeters < 15

# Initialization of Sensors & Sensor Vars
RMC.off()
LMC.off()
leds.all_off()

cl.mode='COL-COLOR'
#cl.mode='RGB-RAW'

'''
leds.all_off()
while True:
    if us.distance_centimeters < 10:
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
    else:
        leds.all_off()
'''

''' 
while True:
    if cl.value() == C_BROWN:
        print("BROWN")
    else:
        print(cl.value())
'''

'''
while True:  
    red = cl.value(0)
    green=cl.value(1)
    blue=cl.value(2)
    print("Red: " + str(red) + ", Green: " + str(green) + ", Blue: " + str(blue))
'''

while cl.value() != HOME:
    nagHumans()
    print("NOT ON HOME")
    print(cl.value())
    sleep(0.25)




# **************************************** MAIN ******************************
print("Finding Next Goal...")
i = 2

while i > 0:
    SPOT = HOME
    if i == 2:
        SPOT = GOAL

    i = i - 1
    hasFoundSpot = False
    while not hasFoundSpot:
        currentColor = cl.value()

        if currentColor != C_BLACK and currentColor != C_NO_COLOR and currentColor != C_WHITE and currentColor == SPOT:
            # Found the spot!
            RMC.off()
            LMC.off()

            RMC.on(-25)
            LMC.on(-25)
            sleep(0.1)
            stopMotors()

            # Double Check Sensor
            idx = 5
            while idx > 0:
                currentColor = cl.value()
                sleep(0.01)
                if currentColor != SPOT:
                    idx = -2
                idx = idx - 1

            if idx != -3:
                nagHumans()
                hasFoundSpot = True
                sleep(1)

        elif isOnBlackLineOrTable(currentColor) or hasBumpedBook():
            # Turn & go
            backUpThenTurn()

        else:
            RMC.on(-50)
            LMC.on(-50)



# Done with Program
RMC.off()
LMC.off()