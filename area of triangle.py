# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 20:26:12 2018

@author: Lalit
"""

a = float(input('Enter first side:'))
b = float(input('Enter second side:'))
c = float(input('Enter third side:'))

s = (a+b+c)/2

area = (s*(s-a)*(s-b)*(s-c))**0.5

print('The area of the triangle is %0.2f' %area)
