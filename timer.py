"""
This program is an edit of the example used for MGTC28.
timer.py is a simple Python script that was changed to play the nerves of steel game.
"""

# This program is used for the nerves of steel game

import time # The time library has a sleep function that will pause the script for a specifized amount of time
import random # The random library has functions to generate a random number

print ("Players stand")

random_time = random.randint(5,25) #generate random integer between 5 and 25

time.sleep(random_time) #sleeps program for the random time generated

print ("Time up. Last to sit down wins")
