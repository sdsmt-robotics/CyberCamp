#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

#####################################

MIN_DIST = 500 # Change this number here

while 1:

    dist = geek.get_ir_distance()
    print(dist)

    if dist <= MIN_DIST:
            geek.beep(1)
            geek.set_ir_position(-90)
            wait(.2)
            dist = geek.get_ir_distance()
            print(dist)

            if dist <= MIN_DIST:
                geek.beep(1)
                geek.set_ir_position(0)
                geek.turn_right(50)
                wait(.8)        # Put your turn right number here
                geek.halt()
            
            else:
                geek.set_ir_position(0)
                geek.turn_left(50)
                wait(.8)        # Put your turn left number here
                geek.halt()
    wait(.2)
#####################################


geek.shutdown()

