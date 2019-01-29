#!/bin/bash

# The color sensor 

# Thanks Internet
# http://docs.ev3dev.org/projects/lego-linux-drivers/en/ev3dev-jessie/sensor_data.html#lego-ev3-color


# Get the sensor by the port
function getColorSensorByPort {
    CS="NULL"
    for i in 0 1 2 3
    do
        tmp=/sys/class/lego-sensor/sensor$i
        if [ "$(cat $tmp/address 2> /dev/null )" = "ev3-ports:$1" ] && [ "$(cat $tmp/driver_name 2> /dev/null )" = "lego-ev3-color" ]; then
            CS=$tmp
        fi
    done

    if [ "$CS" = "NULL" ]; then
        1>&2 echo ----------The color sensor on port $1 wasn\'t found
    fi

    echo $CS
}

# Echo the color detected by the sensor
function echoCurrentColor {
    echo RGB-RAW > $CS/mode
    Red="$(cat $CS/value0 2> /dev/null)"
    Green="$(cat $CS/value1 2> /dev/null)"
    Blue="$(cat $CS/value2 2> /dev/null)"

    echo Red: $Red   Green: $Green    Blue: $Blue
}