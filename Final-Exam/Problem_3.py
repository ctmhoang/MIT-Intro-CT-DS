#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 06:35:21 2019

@author: artlist
"""

# Problem 3-1
# 4.0/4.0 points (graded)
# You have a bucket with 4 red balls and 4 green balls. You draw 3 balls out of the bucket. Assume that once you draw a ball out of the
# bucket, you don't replace it. What is the probability of drawing 3 balls of the same color? Answer the question in reduced fraction
# form - eg 1/5 instead of 2/10.

# 1/7
# correct


# Problem 3-2
# 16.0/16.0 points (graded)
# Write a Monte Carlo simulation to solve the above problem. Feel free to write a helper function if you wish.

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.


import random

# Paste your code here
def drawing_without_replacement_sim(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    4 red and 4 green balls. Balls are not replaced once
    drawn. Returns a float - the fraction of times 3 
    balls of the same color were drawn in the first 3 draws.
    '''
    # Your code here
    qual = [["R",4], ["G", 4]]
    balls = [ball for _ in qual for ball in [_[0]]*_[1]]
    counter = 0
    for _ in range(numTrials):
        clone = balls[:]
        drewBalls = []
        for i in range(3):
            drewBalls.append(random.choice(clone))
            if drewBalls[-1] == drewBalls[0]:
                clone.remove(drewBalls[-1])
            else: 
                break
            if len(drewBalls) == 3:
                counter += 1
    return counter / numTrials
            
