# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:34:45 2018

@author: Lalit
"""

x = input('Enter value of x:')
y = input('Enter value of y:')

temp = x
x = y
y = temp

print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))