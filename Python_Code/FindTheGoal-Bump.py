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
from ev3dev2.sensor import INPUT_1, INPUT_4
from ev3dev2.sensor.lego import TouchSensor
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
ts = TouchSensor()


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
        if i % 3 == 0 or i % 5 == 0:
            sound.tone(  [  (1000, 100, 0),  (1000, 100, 0),  (100, 100, 0),  (100, 100, 0)  ]  )

        leds.set_color('RIGHT', 'GREEN')
        leds.set_color('LEFT', 'GREEN')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        i = i - 1
    
    leds.all_off()

def checkForSpot(SPOT):
    # Found the spot!
    RMC.off()
    LMC.off()

    RMC.on(-25)
    LMC.on(-25)
    sleep(0.1)
    stopMotors()

    # Double Check Sensor
    idx = 10
    while idx > 0:
        currentColor = cl.value()
        sleep(0.1)
        if currentColor != SPOT:
            idx = -2
        idx = idx - 1

    if idx != -3:
        stopMotors()
        nagHumans()
        sleep(2)
        straightLine = 0
        return True

    return False

def backUpThenTurn(spot):
    RMC.on(25)
    LMC.on(25)
    sleep(6 * random.random())
    RMC.on(25)
    LMC.on(-25)

    done=False
    stopAt = int(round(time.time() * 1000)) + (random.random() * 5 * 1000)
    while (int(round(time.time() * 1000)) - stopAt <= 0) and not done:
        sleep(0.01)
        currentColor = cl.value()
        if currentColor == spot:
            stopMotors()
            retVal = checkForSpot(spot)
            if(retVal):
                return retVal
            else:
                RMC.on(25)
                LMC.on(-25)

    return False

# Table is detected as yellow/brown
# Line may be detected as black, no color, or green ... idk why green
def isOnBlackLineOrTable(currentColor):
    return currentColor == C_BLACK or currentColor == C_NO_COLOR or currentColor == C_GREEN or currentColor == C_YELLOW or currentColor == C_BROWN

def hasBumpedBook():
    return False

turnAmnt=2.3

def turnRight():
    RMC.on(25)
    LMC.on(-25)
    sleep(turnAmnt)


def turnLeft():
    RMC.on(-25)
    LMC.on(25)
    sleep(turnAmnt)

def isBookNearBy():
    return False

# Initialization of Sensors & Sensor Vars
RMC.off()
LMC.off()
leds.all_off()

cl.mode='COL-COLOR'

while cl.value() != HOME:
    nagHumans()
    print("NOT ON HOME" + str(cl.value()))
    sleep(0.25)




# **************************************** MAIN ******************************

i = 2

while i > 0:
    print("Finding Next Goal..." + str(i))
    SPOT = HOME
    if i == 2:
        SPOT = GOAL

    i = i - 1
    hasFoundSpot = False
    straightLine = 0
    goRight=True
    bookTurns=5
    while not hasFoundSpot:
        currentColor = cl.value()

        if currentColor != C_BLACK and currentColor != C_NO_COLOR and currentColor != C_WHITE and currentColor == SPOT:
            hasFoundSpot = checkForSpot(SPOT)
            straightLine = 0

        elif hasBumpedBook() or isBookNearBy() or straightLine > 3000 or ts.value():
            if bookTurns <= 5:
                bookTurns = bookTurns + 1
                turnRight()
                RMC.on(-100)
                LMC.on(-100)
                sleep(1)
                turnLeft()
            else:
                if backUpThenTurn(SPOT):
                    hasFoundSpot = True

                straightLine = 0

        elif isOnBlackLineOrTable(currentColor):
            # Turn & go
            if backUpThenTurn(SPOT):
                hasFoundSpot = True

            straightLine = 0

        else:
            RMC.on(-100)
            LMC.on(-100)

            if straightLine % 5 == 0:
                goRight = not goRight

            sleep(0.01)
            straightLine = straightLine + 1



# Done with Program
RMC.off()
LMC.off()