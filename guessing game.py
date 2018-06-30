# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 16:54:49 2018

@author: Lalit
"""

import random

comGuess = random.randint(0,100)

while True:
    userGuess = int(input("Guess a number between 0-100"))
    if userGuess>comGuess:
        print("Guess lower")
    elif userGuess<comGuess:
        print("Guess higher")
    else:
        print("Congrats, correct answer")
        
        break