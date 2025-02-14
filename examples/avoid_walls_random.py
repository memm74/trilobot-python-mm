#!/usr/bin/env python3

from trilobot import Trilobot, BUTTON_A
import random
import time

"""
Further demonstrating Trilobot's ultrasound distance sensor, this example will drive
forward and then turn right to avoid obstacles it detects them with the sensor.

Stop the example by pressing button A.
"""
print("Trilobot Example: Avoid Walls\n")


SPEED = 0.7  # The speed to drive at
TURN_DISTANCE = 30  # How close a wall needs to be, in cm, before we start turning

tbot = Trilobot()

direction = ['left', 'right']
turn_direction = random.choice(direction)
attempts = 0

# Start moving forward
tbot.forward(SPEED)

while not tbot.read_button(BUTTON_A):
    distance = tbot.read_distance()

    # Turn if closer than the turn distance
    if distance < TURN_DISTANCE:
        tbot.backward(SPEED)  # Drive backward
        time.sleep(0.)  # Sleep to move back a bit

        #stick with the direction decision to avoid oscillation
        if attempts == 0:
            turn_direction = random.choice(direction)
            attempts = 10

        if turn_direction == 'left':
            tbot.turn_left(SPEED)
        else:
            tbot.turn_right(SPEED)

        attempts -= 1
    else:
        tbot.forward(SPEED)
    # No sleep is needed, as distance sensor provides sleep
