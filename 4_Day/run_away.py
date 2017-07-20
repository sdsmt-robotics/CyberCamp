#!/usr/bin/env python

import geekbot
import sys
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

######################################

def turn_left_90():
    geek.turn_left()
    wait(.8)
    geek.halt()

def turn_right_90():
    geek.turn_right()
    wait(.8)
    geek.halt()

MIN_DIST = 15

while 1:                                # Loop
    try:
        geek.drive_forward(50, -6)      # Drive
        dist = geek.get_ir_distance()   # Get ir distance
        print(dist)                     # Print the distance out to the screen

        if dist <= MIN_DIST:            # If an object is too close
            geek.halt()                 # Stop moving
            wait(.2)                    # Wait a moment
            geek.beep(1)                # Beep
            geek.turn_right(50)         # Turn right
            wait(1.7)                   #    180 degrees
            geek.halt()                 # Stop moving

    except KeyboardInterrupt: # Handle the ctrl + c
        geek.shutdown()
        break












######################################
