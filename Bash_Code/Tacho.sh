#!/bin/bash
# Include this file in another bash script
# to get access to motors abstractly
#



# set the speed of a motor controller
#
# Example:
# setSpeed $RMC $speed
function setSpeed {
    if [ "$1" = "NULL" ]; then
        1>&2 echo --------- Motor controller is invalid
        return 1
    fi
    echo run-forever > $1/command
    echo $2 > $1/speed_sp
    echo run-forever > $1/command
}

# set the speed of two motor controller
#
# Example:
# setSpeed $RMC $speed $LMC $speed
function setSpeeds {
    if [ "$1" = "NULL" ]; then
        1>&2 echo --------- Motor controller is invalid
        return 1
    fi
    echo run-forever > $1/command
    echo $2 > $1/speed_sp
    echo run-forever > $1/command

    echo run-forever > $3/command
    echo $4 > $3/speed_sp
    echo run-forever > $3/command
}

# Reset the motor controller to a known state
# eg stop the motor
#
# Example:
# resetMotorController $RMC
function resetMotorController {
    if [ "$1" = "NULL" ]; then
        1>&2 echo --------- Motor controller is invalid
        return 1
    fi
    echo reset > $1/command
}

# Get a motor controller by the port it's attached to
#
# Example:
# $RMC=$(getMotorControllerByPort outD)
function getMotorControllerByPort {
    MC="NULL"
    for i in 0 1 2 3
    do
        tmp=/sys/class/tacho-motor/motor$i
        if [ "$(cat $tmp/address 2> /dev/null )" = "ev3-ports:$1" ]; then
            MC=$tmp
        fi
    done

    if [ "$MC" = "NULL" ]; then
        1>&2 echo ----------The motor on port $1 wasn\'t found
    fi

    echo $MC
}