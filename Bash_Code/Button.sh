#!/bin/bash

# Code to use the button

# Get the button by the port
function getButtonByPort {
    CS="NULL"
    for i in 0 1 2 3
    do
        tmp=/sys/class/lego-sensor/sensor$i
        if [ "$(cat $tmp/address 2> /dev/null )" = "ev3-ports:$1" ] && [ "$(cat $tmp/driver_name 2> /dev/null )" = "lego-ev3-touch" ]; then
            CS=$tmp
        fi
    done

    if [ "$CS" = "NULL" ]; then
        1>&2 echo ----------The button on port $1 wasn\'t found
    fi

    echo $CS
}

# Returns the string '0' if not
# or '1' if pressed
function isButtonPressed {
    cat $1/value0 2> /dev/null
}