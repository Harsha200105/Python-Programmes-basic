# -*- coding: utf-8 -*-
"""
Created on Mon Jun  4 18:04:39 2018

@author: Lalit
"""

my_str = input("Enter a string")

words = my_str.split()

words.sort()


print("The sorted words are:")

for word in words:
    print(word)