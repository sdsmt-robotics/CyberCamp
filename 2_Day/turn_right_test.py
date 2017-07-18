#!/usr/bin/env python 

import geekbot
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

i = 0

while i < 4:

##########################
# If the code finishes and the robot has returned to 
# its original position, you've made 4 90 degree turns!

# Use the 'turn' function with a value between 0 and 100 for a right hand turn
    geek.turn(50)

# Use the 'wait' function to give the robot time to turn
    wait(2.9)

# Use the 'halt' function to stop the robot
    geek.halt()
    wait(.5)
##########################

    i += 1

geek.shutdown()
