#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 01 15:41:27 2019

@author: artlist
"""

import math

# Uncomment it if u want to test numpy ver
#import os
#os.environ["OPENBLAS_NUM_THREADS"] = "1"
#import numpy as np

def stdDevOfLengths(L):
    """
    L: a list of strings

    returns: float, the standard deviation of the lengths of the strings,
      or NaN if L is empty.
    """
    if len(L) != 0:
        lN = list(map(lambda l: len(l), L))
        mean = (sum(i for i in lN)) / len(L)
        stdDev = math.sqrt(sum((i - mean)**2 for i in lN) / len(L))
        return stdDev
    else:
        return float('nan')
    
#Numpyway
# def stdDevOfLengths(L):
#   return np.std(list(map(lambda l: len(l), L)))

#    Test case: If L = ['a', 'z', 'p'], stdDevOfLengths(L) should return 0.
#
#    Test case: If L = ['apples', 'oranges', 'kiwis', 'pineapples'], stdDevOfLengths(L) should return 1.8708.

