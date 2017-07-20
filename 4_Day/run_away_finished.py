#!/usr/bin/env python

import geekbot
import sys
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

######################################

def turn_left_90():
    geek.turn_left(50)
    wait(.8)
    geek.halt()

def turn_right_90():
    geek.turn_right(50)
    wait(.8)
    geek.halt()

MIN_DIST = 15

while 1:                                    # Loop
    try:
        geek.drive_forward(50, -6)          # Drive
        dist = geek.get_ir_distance()       # Get ir distance
        print(dist)                         # Print the distance out to the screen

        if dist <= MIN_DIST:                # If an object is too close
            geek.halt()                     # Stop moving
            geek.beep(1)                    # Beep
            geek.set_ir_position(-90)       # Look left
            wait(.2)
            dist = geek.get_ir_distance()   # Get distance
            print(dist)

            if dist <= MIN_DIST:
                wait(.2)
                geek.beep(1)
                geek.set_ir_position(0)
                turn_right_90()
            else:
                wait(.2)
                geek.set_ir_position(0)
                turn_left_90()


    except KeyboardInterrupt: # Handle the ctrl + c
        geek.shutdown()
        break

######################################
