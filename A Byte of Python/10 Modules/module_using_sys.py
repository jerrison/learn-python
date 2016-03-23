# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 13:07:40 2016

@author: Jerrison Li
"""

import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)
    
print('\n\nThe PYTHONPATH is', sys.path, '\n')