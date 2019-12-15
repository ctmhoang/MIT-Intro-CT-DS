#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 21:12:42 2019

@author: artlist
"""

import random, pylab

# You are given this function
def getMeanAndStd(X):
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

# You are given this class
class Die(object):
    def __init__(self, valList):
        """ valList is not empty """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

# Implement this -- Coding Part 1 of 2
def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    # TODO
    pylab.hist(values, bins = numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title, loc ="center")
    pylab.show()
    
                    
# Implement this -- Coding Part 2 of 2
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated to 3 decimal places
    """
    # TODO
    longestDict = []
    for i in range(numTrials):
        rolls = [die.roll() for _ in range(numRolls)]
        longestDict.append(longest_run(rolls))
    makeHistogram(longestDict, numBins = 10, xLabel = 'Length of longest run', yLabel = 'frequency', title = 'Histogram of longest runs')
    return sum(longestDict)/numTrials
    
def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can be
    A run of numbers counts the number of times the same dice value shows up
    in consecutive rolls.
    Does not modify the list.
    Returns the total element of longest run.
    """
    maxCount = 0
    strIndex, endIndex = 0,1
    while strIndex <len(L):
        temp =L[strIndex:endIndex]
        if haveAllSameValue(temp) and maxCount < len(temp):
            maxCount = len(temp)
            endIndex += 1
        else:
            strIndex += 1
            endIndex += 1
            
    return maxCount

def haveAllSameValue(L):
    """
    Assumes L is a list 
    Return True if all values in list are the same
    False otherwise
    """
    return all(x ==L[0] for x in L)
        
    
# One test case
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 500, 10000))
print(getAverage(Die([1,2,3,4,5,6]), 50, 1000))
print(getAverage(Die([1,2,3,4,5,6,6,6,7]), 1, 1000))