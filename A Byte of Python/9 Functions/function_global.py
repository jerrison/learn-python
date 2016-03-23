# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 11:27:57 2016

@author: Jerrison Li
"""

x = 50

def func():
    global x
    
    print('x is', x)
    x = 2
    print('Changed global x to', x)
    
    
func()
print('Value of x is', x)