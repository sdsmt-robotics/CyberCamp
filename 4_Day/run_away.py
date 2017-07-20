#!/usr/bin/env python

import geekbot
import sys
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

######################################

def turn_left_90():    # We'll use this function to automate making a perfect left 90 turn
    geek.turn_left(50) # put your speed for turning in here (default: 50)
    wait(.8)           # put your delay for a perfect left 90 here 
    geek.halt()

def turn_right_90(): # same as above
    geek.turn_right(50)
    wait(.8)
    geek.halt()

MIN_DIST = 15 # this is our "wow that thing is too close" distance

while 1:                                # Loop
    try:
        wait(0.1)                       # Controls how fast we read the sensor (how often we loop)
        geek.drive_forward(50, -6)      # Remind to drive (put in your corrections from day 2)
        dist = geek.get_ir_distance()   # Get ir distance ( 7 - 40cm if a good reading, -1 if bad)
        print(dist)                     # Print the distance out to the screen

        if dist != -1 and dist <= MIN_DIST: # If we get a valid sensor reading AND it's close
                                            # enough to cause concern
            geek.halt()                 # Stop moving
            wait(.2)                    # Wait a moment
            geek.beep(1)                # Beep
            turn_right_90()             # Turn right
            turn_right_90()             # Turn right again! (that makes 180 degrees? right?)
        # Remember: you can always put if statments inside of other if statements! Just make sure
        # things are indented correctly and don't forget the colon. These "nested" if statements
        # are really handy for doing things like looking around to find open spaces!

####################################################################
    except KeyboardInterrupt: # Handle the ctrl + c
        geek.shutdown()
        sys.exit()












######################################
