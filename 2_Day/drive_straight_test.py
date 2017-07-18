#!/usr/bin/env python

import geekbot
from time import sleep as wait

geek = geekbot.Robot("/dev/ttyUSB0", 57600)

###########################

# Here, use the 'drive_forward' function and change the 'adjust'
# parameter (the second one) so your robot drives straight
# Negative = turn more right
# Positive = turn more left
geek.drive_forward(50, -15)

# Use the 'wait' function to let the geekbot drive for a while
wait(3)

# Use the 'halt' function to stop your robot
geek.halt()

###########################

geekbot.shutdown()
