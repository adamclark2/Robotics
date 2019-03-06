#!/usr/bin/python3

# Find The Goal Simple
# By:
# Adam Clark <adam.clark2@maine.edu>
#
# When started on a colored piece of paper
# it will find another piece of paper &
# return to its original paper. Simple doesn't detect obsticles 
#
# RED is Home
# BLUE is Goal

import os

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D, SpeedPercent, MoveTank
from ev3dev2.sensor.lego import ColorSensor
from ev3dev2.sensor.lego import GyroSensor
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

HOME = C_RED
GOAL = C_BLUE

print("Program Running...")

# Sensor Constructors
cl = ColorSensor() 
gy = GyroSensor()
leds = Leds()
sound = Sound()
RMC = LargeMotor(OUTPUT_D)
LMC = LargeMotor(OUTPUT_A)

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
            #sound.tone(  [  (1000, 100, 0),  (1000, 100, 0),  (100, 100, 0),  (100, 100, 0)  ]  )

        leds.set_color('RIGHT', 'GREEN')
        leds.set_color('LEFT', 'GREEN')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        i = i - 1
    
    leds.all_off()
    

def turnAround():
    RMC.on(-25)
    LMC.on(-25)
    sleep(1)

    RMC.off()
    LMC.off()
    sleep(0.01)
    start = gy.value()

    RMC.on(-10)
    LMC.on(10)
    while(abs(start - gy.value()) <= 90):
        sleep(0.001)

    RMC.off()
    LMC.off()

# Initialization of Sensors & Sensor Vars
RMC.off()
LMC.off()
leds.all_off()

cl.mode='COL-COLOR'
gy.mode='GYRO-ANG'

while cl.value() != HOME:
    nagHumans()
    sleep(0.25)


# **************************************** MAIN ******************************
foundGoal = False
right = 1
start = int(round(time.time() * 1000))
while not foundGoal:
    RMC.on(right)
    LMC.on(100)
    if int(round(time.time() * 1000)) - start >= 250:
        right = right + 1
        if right > 100:
            right = 100
        print("Faster by " + str(right))
        start = int(round(time.time() * 1000))
    if cl.value() == C_BLACK or cl.value() == C_NO_COLOR:
        turnAround()
    if cl.value() == GOAL:
        RMC.off()
        LMC.off()
        nagHumans()
        foundGoal = True

foundGoal = False
right = 1
start = int(round(time.time() * 1000))
while not foundGoal:
    RMC.on(right)
    LMC.on(100)
    if int(round(time.time() * 1000)) - start >= 250:
        right = right + 1
        if right > 100:
            right = 100
        print("Faster by " + str(right))
        start = int(round(time.time() * 1000))
    if cl.value() == C_BLACK or cl.value() == C_NO_COLOR:
        turnAround()
    if cl.value() == HOME:
        RMC.off()
        LMC.off()
        nagHumans()
        foundGoal = True



# Done with Program
RMC.off()
LMC.off()
nagHumans()

print("****PROGRAM DONE****")