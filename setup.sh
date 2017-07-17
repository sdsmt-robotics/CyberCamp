#!/bin/bash

curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py

sudo pip install pyserial

sudo adduser $USER dialout

gnome-session-quit

