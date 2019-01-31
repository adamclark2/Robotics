#!/bin/bash

# Includes
source Tacho.sh

# Useful Globals
speed=1050
turnSpeed=700

# A RemoteControl Written in bash...
# c++ didn't work well...
# we could use files insted of the library online
#
# Useful Link:
# https://www.ev3dev.org/docs/tutorials/tacho-motors/


# Reset terminal on exit
# We need to disable canonical mode
trap "stty $(stty -g)" EXIT
stty -echo -icanon time 2 || exit $?


# Right/Left Motor Controller
RMC="$(getMotorControllerByPort outD)"
LMC="$(getMotorControllerByPort outA)"


echo Use WASD to control the robot. \'e\' stops the robot.
echo Ctrl+C to quit or press \'q\'
echo -------------------------------------------------------
echo
echo Do you want to press to stop?
U_PUSH_TO_STOP="NULL"
while [ "$U_PUSH_TO_STOP" != "y" ] && [ "$U_PUSH_TO_STOP" != "n" ]; do
    echo [y/n]
    read -n 1 -a U_PUSH_TO_STOP
done
echo $U_PUSH_TO_STOP was chosen.

while [ 1 ]; do
    U_INPUT="X"
    read -n 1 -a U_INPUT -t 1
    if [ "$U_INPUT" = "q" ]; then
        echo Adios
        setSpeeds $RMC 0 $LMC 0
        exit 0

    elif [ "$U_INPUT" = "w" ]; then
        setSpeeds $RMC $speed $LMC $speed

    elif [ "$U_INPUT" = "s" ]; then
        setSpeeds $RMC -$speed $LMC -$speed

    elif [ "$U_INPUT" = "a" ]; then
        setSpeeds $RMC $turnSpeed $LMC -$turnSpeed

    elif [ "$U_INPUT" = "d" ]; then
        setSpeeds $RMC -$turnSpeed $LMC $turnSpeed

    elif [ "$U_INPUT" = "e" ]; then
        setSpeeds $RMC 0 $LMC 0

    else # Full Stop
        if [ "$U_PUSH_TO_STOP" = "n" ]; then
            setSpeeds $RMC 0 $LMC 0
        fi
    fi
done 


# Bad stuff happened here!
exit 1