# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 16:08:48 2018

@author: Lalit
"""

lower = int(input("enter a lower range:"))
upper = int(input("enter a upper range:"))

print("prime numbers between", lower, "and", upper, "are:")

for num in range(lower,upper+1):
    
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
            
        else:
            
            print(num)