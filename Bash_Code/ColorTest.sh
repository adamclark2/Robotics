#!/bin/bash

# Includes
source ColorSensor.sh

# Test the color sensor
CS="$(getColorSensorByPort in1)"

echo $CS

while [ 1 ]; do
    echoCurrentColor $CS
    sleep 0.25
done