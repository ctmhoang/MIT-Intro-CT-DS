#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 08:02:29 2019

@author: artlist
"""

# Problem 6
# Bookmark this page
# Problem 6
# 20.0/20.0 points (graded)
# Write a function that meets the specifications below. You do not have to use dynamic programming.

# Hint: You might want to use bin() on an int to get a string, get rid of the first two characters, add leading 0's as needed, and then
# convert it to a numpy array of ints. Type help(bin) in the console.

# For example,
# If choices = [1,2,2,3] and total = 4 you should return either [0 1 1 0] or [1 0 0 1]
# If choices = [1,1,3,5,3] and total = 5 you should return [0 0 0 1 0]
# If choices = [1,1,1,9] and total = 4 you should return [1 1 1 0]

# More specifically, write a function that meets the specifications below:
#def find_combination(choices, total):
#    """
#    choices: a non-empty list of ints
#    total: a positive int
# 
#    Returns result, a numpy.array of length len(choices) 
#    such that
#        * each element of result is 0 or 1
#        * sum(result*choices) == total
#        * sum(result) is as small as possible
#    In case of ties, returns any result that works.
#    If there is no result that gives the exact total, 
#    pick the one that gives sum(result*choices) closest 
#    to total without going over.
#    """
    
# Paste your entire function (including the definition) in the box. Note: If you want to use numpy arrays, you should import numpy as np
# and use np.METHOD_NAME in your code. Unfortunately, pylab does not work with the grader.


import numpy as np
import itertools
    
def find_combination(choices, total):
    """
    choices: a non-empty list of ints
    total: a positive int
 
    Returns result, a numpy.array of length len(choices) 
    such that
        * each element of result is 0 or 1
        * sum(result*choices) == total
        * sum(result) is as small as possible
    In case of ties, returns any result that works.
    If there is no result that gives the exact total, 
    pick the one that gives sum(result*choices) closest 
    to total without going over.
    """
    coefficentsGaveLessRes = []
    optimalCoefficents = []
    choice = np.array(choices)
    for _ in itertools.product([1,0], repeat = len(choices)):
        #Creates all possible lists made up of eles in gave list 
        if sum(_*choice) == total:
            optimalCoefficents.append(_)
        elif sum(_*choice) < total:
            coefficentsGaveLessRes.append(_)
    if optimalCoefficents != []:
        return np.array(min(optimalCoefficents, key = lambda x: sum(x)))
    else:
        return np.array(max(coefficentsGaveLessRes, key = lambda x: sum(x)))
