# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:46:03 2016

@author: Jerrison Li
"""

def maximum(x, y):
    if x > y:
        return x
    elif x == y:
        return 'The numbers are equal'
    else:
        return y
        

print(maximum(2, 3))
print(maximum(10, 3))
print(maximum(10, 10))
