# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:58:30 2018

@author: Lalit
"""

import itertools, random

deck = list(itertools.product(range(1,14),

['Spade','Heart','diamond', 'Club']))

random.shuffle(deck)

print("you got:")

for i in range(8):
    print(deck[i][0], "of", deck[i][1])