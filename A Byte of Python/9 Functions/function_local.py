# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:25:03 2016

@author: lijerri1
"""

x = 50

def func(x):
    print('x is', x)
    x = 2
    print('Changed local x to', x)
    
func(x)
print('x is still', x)