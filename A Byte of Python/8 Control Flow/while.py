# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 13:28:41 2016

@author: lijerri1
"""

number = 23
running = True

while running:
    guess = int(input('Enter an integer: '))
    
    if guess == number:
        print('Congratulations, you guessed it.')
        # this causes the while loop to stop
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
        
else:
    print('The while loop is over.')
    # Do anything else you want do do here
    
print('Done')