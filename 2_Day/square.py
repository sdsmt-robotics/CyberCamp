#!/usr/bin/env python

import geekbot

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

i = 0

# We're going to drive forward, stop, turn right, and stop four 
# times. The goal is to driv the robot in square
while i < 4:

############################

    # Use the adjustment and speed you found in 
    # 'drive_straight_test.py' to have the robot
    # drive straight for a bit
    geek.drive_forward(50,-15)
    wait(2)
    
    # Let the robot come to a full stop
    geek.halt()
    wait(.5)
    
    # Use the time you found in 'turn_right_test.py'
    # to have the robot make a perfect 90 degree turn
    geek.turn_right(50)
    wait(2.9)
    
    # Once the turn is complete, come to a complete stop
    geek.halt()
    wait(.5)

    # Automatically increment the counter and do it again!
    i += 1

############################

# Hopefully by this point your robot has moved in a perfect square!
geek.shutdown()

