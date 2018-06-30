# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:08:16 2018

@author: Lalit
"""

 
num = int(input("Enter a number:"))
 
factorial = 1
 
if num < 0 :
    print("factorial not exist")
    
elif num == 0:
    print("factorial is 1")
    
else:
    for i in range(1,num+1):
        factorial = factorial*i
        
    print("The factorial of", num, "is", factorial) 
    