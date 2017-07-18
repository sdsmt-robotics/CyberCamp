#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

i = 0

while i < 4:

############################

    # Use the adjustment you found in 'drive_straight_test.py'
    geek.drive_forward(50,-15)
    wait(2)

    geek.halt()
    wait(.5)
    
    geek.turn(50)
    # Use the time you found in 'turn_right_test.py'
    wait(2.9)
    
    geek.halt()
    wait(.5)

############################

    i += 1

geek.shutdown()

