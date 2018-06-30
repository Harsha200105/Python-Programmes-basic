# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:03:20 2018

@author: Lalit
"""

num = int(input("Enter a number: "))

if num > 1:
    
    for i in range(2,num):
        if(num%i) ==0:
            print(num, "is not a prime number")
            
            break
        
    else:
        
        print(num, "is a prime number")