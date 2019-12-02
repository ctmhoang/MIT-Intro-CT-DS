#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 01 18:23:06 2019

@author: artlist
"""

import random
def noReplacementSimulation(numTrials):
    '''
    Runs numTrials trials of a Monte Carlo simulation
    of drawing 3 balls out of a bucket containing
    3 red and 3 green balls. Balls are not replaced once
    drawn. Returns the a decimal - the fraction of times 3 
    balls of the same color were drawn.
    '''
    # Your code here
    numGet = 0
    def pGet3bSameColor():
        '''
        Simulates one trial of drawing 3 balls out of a bucket containing
        3 red and 3 green balls. Balls are not replaced once
        drawn. Returns True if all three balls are the same color,
        False otherwise.
        '''
        bs = [c for i in range(3) for c in ['g','b']]
        preChoice, curChoice = None, None
        for _ in range(3):
            if (preChoice == curChoice) or (preChoice == None):
                preChoice = curChoice
                curChoice = random.choice(bs)
                bs.remove(curChoice)
            else:
                return False
        return True
    for _ in range(numTrials):
        if pGet3bSameColor():
            numGet += 1
    return numGet/numTrials
