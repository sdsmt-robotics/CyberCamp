#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

#####################################

while 1:
    dist = geek.get_ir_distance()
    print(dist)
    if dist <= 20:
            geek.beep(1)
            geek.set_ir_position(-90)
            wait(.2)
            dist = geek.get_ir_distance()
            print(dist)
            if dist <= 20:
                geek.beep(1)
                geek.set_ir_position(0)
                geek.turn_right(50)
                wait(.8)
                geek.halt()
            else:
                geek.set_ir_position(0)
                geek.turn_left(50)
                wait(.8)
                geek.halt()
    wait(.2)
#####################################


geek.shutdown()

