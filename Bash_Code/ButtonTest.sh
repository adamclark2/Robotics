#!/bin/bash

# Includes
source Button.sh

# Test the button

BTN="$(getButtonByPort in2)"

while [ 1 ]; do
    if [  "$(isButtonPressed $BTN)" = "1" ]; then
        echo OUCH
    fi
done