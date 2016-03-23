# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:05:16 2016

@author: lijerri1
"""

while True:
    s = input('Enter something: ')
    if s == 'quit':
        break
    if len(s) < 3:
        print('Too small')
        continue
    print('Input is of sufficient length')
    # Do other kinds of processing here