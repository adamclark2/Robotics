#!/usr/bin/python3

# Printer
# By:
# Adam Clark <adam.clark2@maine.edu>
#
# A EV3 printer. This will draw on a receipt sized peice of paper.

import os

from ev3dev2.motor import LargeMotor, MediumMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, SpeedPercent, MoveTank
from ev3dev2.led import Leds
from ev3dev2.sensor.lego import TouchSensor
from time import sleep
import random

import signal
import sys

print("Program Running...")

# Sensor Constructors
leds = Leds()
paperMotor = MediumMotor(OUTPUT_B)
markerMotor = LargeMotor(OUTPUT_A)
carrageMotor = LargeMotor(OUTPUT_C)
ts = TouchSensor()

# Constants and Vars
carrageBound1 = 0
carrageBound2 = 0
deltaBound = 0

# Position of the carrage
# 1 to 10
carragePosition = 0


# Function Defs
def stopMotors():
    leds.all_off()
    paperMotor.off()
    markerMotor.off()
    carrageMotor.off()
    paperMotor.stop(stop_action = 'coast')
    markerMotor.stop(stop_action = 'coast')
    carrageMotor.stop(stop_action = 'coast')

import atexit
atexit.register(stopMotors)

def signal_handler(sig, frame):
        print('You pressed Ctrl+C!')
        stopMotors()
        sys.exit(0)
        
signal.signal(signal.SIGINT, signal_handler)

def nagHumans():
    i = 5
    while i >= 0:
        leds.set_color('RIGHT', 'GREEN')
        leds.set_color('LEFT', 'GREEN')
        sleep(0.1)
        leds.set_color('RIGHT', 'RED')
        leds.set_color('LEFT', 'RED')
        sleep(0.1)
        i = i - 1
    
    leds.all_off()


def markerDown():
    markerMotor.on(25)
    while not markerMotor.is_stalled:
        # idle
        sleep(0.001)

    markerMotor.stop(stop_action = 'coast')

def markerUp():
    markerMotor.on(-25)
    while not markerMotor.is_stalled:
        # idle
        sleep(0.001)

    markerMotor.stop(stop_action = 'coast')

def lineFeed():
    paperMotor.run_to_rel_pos(position_sp=-10, speed_sp=900, stop_action="hold")
    sleep(0.05)

def lineReverse():
    paperMotor.run_to_rel_pos(position_sp=10, speed_sp=900, stop_action="hold")
    sleep(0.05)

def isCarrageOutOfBounds():
    if carrageBound1 < carrageBound2:
        return carrageMotor.position >= carrageBound2 or carrageMotor.position <= carrageBound1
    else:
        return carrageMotor.position <= carrageBound2 or carrageMotor.position >= carrageBound1

def carrageAdvance():
    global carragePosition

    carrageMotor.run_to_rel_pos(position_sp=(deltaBound / 3), speed_sp=1000, stop_action="hold")
    carragePosition = carragePosition + 1
    if carragePosition > 10:
        print("The carrage has gon off the track.")
    else:
        print("     Carrage Advance: " + str(carragePosition))

    sleep(0.2)

def carrageReturn():
    global carragePosition

    print("Carrage Return")
    carrageMotor.on(-35)
    sleep(0.1)
    while carrageMotor.position > carrageBound1:
        sleep(0.001)
    carrageMotor.off()
    carragePosition = 0
    sleep(0.001)

    # Advance to eliminate gear play
    # in the worm gear
    carrageMotor.run_to_rel_pos(position_sp=180, speed_sp=100, stop_action="hold")
    sleep(0.1)



# ______________________________________ MAIN ______________________________________
try:
    
    # A zig zag stair case pattern
    for z in range(0, 3):
        markerDown()
        for x in range(0,5):
            print("X:= " + str(x))
            carrageMotor.on(-25)
            sleep(0.25)
            carrageMotor.off()
            lineFeed()

        lineFeed()
        lineFeed()
        lineFeed()

        for x in range(0,5):
            print("X:= " + str(x))
            carrageMotor.on(25)
            sleep(0.25)
            carrageMotor.off()
            lineFeed()


    # This code draws three rows of lines
    '''
    for x in range(0,3):
        markerDown()
        carrageMotor.on(-25)
        sleep(0.25)

        carrageMotor.off()
        markerUp()
        carrageMotor.on(-25)
        sleep(0.25)

        carrageMotor.off()
        markerDown()
        carrageMotor.on(-25)
        sleep(0.25)

        carrageMotor.off()
        lineFeed()

        markerUp()
        carrageMotor.on(25)
        sleep(0.25 * 3)
        carrageMotor.off()
        '''



    



finally:
    stopMotors()

stopMotors()
print("Program Done")