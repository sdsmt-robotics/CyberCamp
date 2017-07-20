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
        wait(.1)                            # Updates the sensor (1/0.1) = 10 times a second
        geek.drive_forward(50, -6)          # Drive forward
        dist = geek.get_ir_distance()       # Get ir distance
        print(dist)                         # Print the distance seen out to the screen

        if dist != -1 and dist <= MIN_DIST: # If we get a valid reading AND 
                                            # the reading is "close enough"

            geek.halt()                     # Stop moving
            geek.beep(1)                    # Beep
            geek.set_ir_position(-90)       # Look left
            wait(.2)
            dist = geek.get_ir_distance()   # Get distance
            print(dist)

            if dist <= MIN_DIST: # Is the left side also blocked? If so do this
                wait(.2)
                geek.beep(1)
                geek.set_ir_position(0)
                turn_right_90()
            else:                # If it's not blocked do this
                wait(.2)
                geek.set_ir_position(0)
                turn_left_90()


    except KeyboardInterrupt: # Handle the ctrl + c
        geek.shutdown()
        break

######################################
