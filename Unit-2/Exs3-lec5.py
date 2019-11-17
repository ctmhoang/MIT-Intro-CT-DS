#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 05:41:24 2019

@author: artlist
"""


import random
def deterministicNumber():
    '''
    Deterministically generates and returns an even number between 9 and 21
    '''
    # Your code here
    return 16

# # Possible solutions:

# def deterministicNumber():
#     return 10 # or 12 or 14 or 16 or 18 or 20

# # or

# def deterministicNumber():
#     random.seed(0) # This will be discussed in the video "Drunken Simulations"
#     return 2 * random.randint(5, 10)

def stochasticNumber():
    '''
    Stochastically generates and returns a uniformly distributed even number between 9 and 21
    '''
    # Your code here
    random.choices(range(10,21,2))

# # Possible solutions:
# def stochasticNumber():
#     return 2 * random.randint(5, 10)

# # or 

# def stochasticNumber():
#     return random.randrange(10, 22, 2)

# # or, again, something like that.
