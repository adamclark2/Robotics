#!/bin/bash

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
for i in 0 1 2 3
do
    tmp=/sys/class/tacho-motor/motor$i
    if [ "$(cat $tmp/address)" = "ev3-ports:outD" ]; then
        RMC=$tmp
    fi
    if [ "$(cat $tmp/address)" = "ev3-ports:outA" ]; then
        LMC=$tmp
    fi
done

# Debug fun!
#RMC=~/Desktop
#LMC=~/Desktop

doExit="no"
if [[ -z ${RMC} ]]; then
    echo RMC is invalid
    doExit="yes"
fi

if [[ -z ${LMC} ]]; then
    echo LMC is invalid
    doExit="yes"
fi

if [ "$doExit" = "yes" ]; then
    echo "See ya"
    exit 1
fi

echo reset > $RMC/command
echo reset > $LMC/command
echo run-forever > $RMC/command
echo run-forever > $LMC/command

echo Use WASD to control the robot. \'e\' stops the robot.
echo Ctrl+C to quit or press \'q\'
echo -------------------------------------------------------
echo
echo Do you want to press to stop?
echo [y/n]

read -n 1 -a U_PUSH_TO_STOP

echo $U_PUSH_TO_STOP was chosen.

function setSpeed {
        echo $1 > $LMC/speed_sp
        echo $2 > $RMC/speed_sp
        echo run-forever > $RMC/command
        echo run-forever > $LMC/command
}

speed=1000
turnSpeed=500

while [ 1 ]; do
    U_INPUT="X"
    read -n 1 -a U_INPUT -t 1
    if [ "$U_INPUT" = "q" ]; then
        echo Adios
        setSpeed 0 0
        exit 0

    elif [ "$U_INPUT" = "w" ]; then
        setSpeed $speed $speed

    elif [ "$U_INPUT" = "s" ]; then
        setSpeed -$speed -$speed

    elif [ "$U_INPUT" = "a" ]; then
        setSpeed -$turnSpeed $turnSpeed

    elif [ "$U_INPUT" = "d" ]; then
        setSpeed $turnSpeed -$turnSpeed

    elif [ "$U_INPUT" = "e" ]; then
        setSpeed 0 0

    else # Full Stop
        if [ "$U_PUSH_TO_STOP" = "n" ]; then
            setSpeed 0 0
        fi
    fi
done 



# Bad stuff happened here!
exit 1