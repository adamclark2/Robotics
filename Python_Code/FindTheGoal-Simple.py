#!/usr/bin/python3

# Find The Goal Simple
# By:
# Adam Clark <adam.clark2@maine.edu>
# Steven Doherty <steven.doherty@maine.edu>
#
# When started on a colored piece of paper
# it will find another piece of paper &
# return to its original paper. Simple doesn't detect obsticles 

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
            # sound.tone(  [  (1000, 100, 0),  (1000, 100, 0),  (100, 100, 0),  (100, 100, 0)  ]  )

        leds.set_color('RIGHT', 'GREEN')
        leds.set_color('LEFT', 'GREEN')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        i = i - 1
    
    leds.all_off()

def turnRight():
    RMC.on(-25)
    LMC.on(-25)
    sleep(0.25)

    start = gy.value()
    RMC.on(-20)
    LMC.on(20)
    while(abs(start - gy.value()) < 90):
        sleep(0.001)

    RMC.off()
    LMC.off()

def turnAround():
    RMC.on(-25)
    LMC.on(-25)
    sleep(1)

    RMC.off()
    LMC.off()
    sleep(0.01)
    start = gy.value()

    RMC.on(-5)
    LMC.on(5)
    while(abs(start - gy.value()) <= 180):
        sleep(0.001)

    RMC.off()
    LMC.off()

def findCorner():
    # Find a corner of the board
    RMC.on(100)
    LMC.on(100)
    while cl.value() != C_BLACK:
        # Idle
        sleep(0.0001)


    turnRight()
    RMC.on(100)
    LMC.on(100)

    while cl.value() != C_BLACK:
        # Idle
        sleep(0.0001)

    RMC.off()
    LMC.off()
    nagHumans()

def hasFoundGoal():
    if cl.value() == GOAL:
        sleep(0.01)
        if cl.value() == GOAL:
            return True

    else:
        return False

# Initialization of Sensors & Sensor Vars
RMC.off()
LMC.off()
leds.all_off()

cl.mode='COL-COLOR'
gy.mode='GYRO-ANG'

#while True:
    #print(gy.value())

while cl.value() != HOME:
    nagHumans()
    sleep(0.25)


# **************************************** MAIN ******************************
foundGoal = False
while not foundGoal:
    RMC.on(50)
    LMC.on(50)
    print("Finding Black Line")

    while cl.value() != C_BLACK and not foundGoal:
        sleep(0.01)

    print("   Found Black Line")

    print("Turning")
    turnAround()
    print("   Done Turning")



# Done with Program
RMC.off()
LMC.off()
nagHumans()

print("****PROGRAM DONE****")