#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 07:13:20 2019

@author: artlist
"""

# Problem 4-2
# 20.0/20.0 points (graded)
# Write a function called getAverage(die, numRolls, numTrials), with the following specification:
#def getAverage(die, numRolls, numTrials):
#    """
#      - die, a Die
#      - numRolls, numTrials, are positive ints
#      - Calculates the expected mean value of the longest run of a number
#        over numTrials runs of numRolls rolls.
#      - Calls makeHistogram to produce a histogram of the longest runs for all
#        the trials. There should be 10 bins in the histogram
#      - Choose appropriate labels for the x and y axes.
#      - Returns the mean calculated to 3 decimal places
#    """

# A run of numbers counts the number of times the same dice value shows up in consecutive rolls. For example:
# a dice roll of 1 4 3 has a longest run of 1
# a dice roll of 1 3 3 2 has a longest run of 2
# a dice roll of 5 4 4 4 5 5 2 5 has a longest run of 3

# When this function is called with the test case given in the file, it will return 5.312. Your simulation may give slightly different
# values.

# Paste your entire function (including the definition) in the box.

# Restrictions:
# Do not import or use functions or methods from pylab, numpy, or matplotlib.
# Do not leave any debugging print statements when you paste your code in the box.
# If you do not see the return value being printed when testing your function, close the histogram window.


# Paste your code here
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
