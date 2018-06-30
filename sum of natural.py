# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 17:51:32 2018

@author: Lalit
"""

num = int(input("Enter a number:"))

if num < 0:
    print("enter a positive umber:")
    
else:
    
    sum = 0
    
    while(num>0):
        sum += num
        num -=1
        
    print("the sum is", sum)
    