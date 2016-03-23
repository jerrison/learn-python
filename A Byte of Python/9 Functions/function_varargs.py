# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:41:00 2016

@author: Jerrison Li
"""

def total(initial = 5, *numbers, **keywords):
    count = initial
    for number in numbers:
        count += number
    for key in keywords:
        count += keywords[key]
    return count
    
print(total(10, 1, 2, 3, vegetables = 50, fruits = 100))