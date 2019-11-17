#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 17 05:40:25 2019

@author: artlist
"""


import random
def genEven():
    '''
    Returns a random even number x, where 0 <= x < 100
    '''
    # Your code here
    return random.randrange(0, 100, 2)
# # There are many good answers to this problem, some easier than others :)
# def genEven():
#     return random.randrange(0, 100, 2)

# def genEven():
#     return random.choice(range(0, 100, 2))

# def genEven():
#     return int(random.random() * 50)*2

# def genEven():
#     return random.choice(range(0, 50))*2

# def genEven():
#     x = random.randint(0, 98)
#     while x % 2 != 0:
#         x = random.randint(0, 98)
#     return x

random.seed()
