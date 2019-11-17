#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun 17 05:34:35 2019

@author: artlist
"""

# Exercise 7

# Exercise 7
# 10/10 points (graded)
# Consider once again our permutations of students in a line. Recall the nodes in the graph represent permutations, and that the edges
# represent swaps of adjacent students. We want to design a weighted graph, weighting edges higher for moves that are harder to make.
# Which of these could be easily implemented by simply assigning weights to the edges already in the graph?

# A) A large student who is difficult to move around in line.
# B) A sticky spot on the floor which is difficult to move onto and off of.

# Write a WeightedEdge class that extends Edge. Its constructor requires a weight parameter, as well as the parameters from Edge. You
# should additionally include a getWeight method. The string value of a WeightedEdge from node A to B with a weight of 3 should be
# "A->B (3)".

class Edge(object):
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()

class WeightedEdge(Edge):
    def __init__(self, src, dest, weight):
        # Your code here
        Edge.__init__(self, src, dest)
        self.weight = weight
    def getWeight(self):
        # Your code here
        self.getWeight = self.weight
        pass
    def __str__(self):
        # Your code here
        return Edge.__str__(self) + " (" + str(self.weight) + ")"
