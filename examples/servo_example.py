#!/usr/bin/env python

import math
import time
from trilobot import Trilobot

tbot = Trilobot()

print("Go to center")
tbot.servo_to_center()
time.sleep(2)

print("Go to min")
tbot.servo_to_min()
time.sleep(2)

print("Go to max")
tbot.servo_to_max()
time.sleep(2)

print("And back to center")
tbot.servo_to_center()
time.sleep(2)

print("Servo Off")
tbot.disable_servo()

print("Now Scan")
while True:
    for i in range(0, 360):
        tbot.set_servo_value(math.sin(math.radians(i)))
        time.sleep(0.01)
