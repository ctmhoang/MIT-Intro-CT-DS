#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 04:36:01 2019

@author: artlist
"""
import random

class RectangularRoom(dict):
    """ subclass dict with clean tile returning True """
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def cleanTileAtPosition(self, pos):
        self[int(pos.x), int(pos.y)] = True
    def isTileCleaned(self, m, n):
        return self.get((m, n), False)
    def getNumTiles(self):
        return self.width * self.height
    def getNumCleanedTiles(self):
        return sum(self.values())
    def getRandomPosition(self):
        return Position(random.randrange(self.width), random.randrange(self.height))
    def isPositionInRoom(self, pos):
        return 0 <= pos.x < self.width and 0 <= pos.y < self.height

class Robot(object):
    def __init__(self, room, speed):
        self.room = room
        self.speed = speed
        self.position = self.room.getRandomPosition()
        self.direction = random.randrange(0, 360)
        self.room.cleanTileAtPosition(self.position)
    def getRobotPosition(self):
        return self.position
    def getRobotDirection(self):
        return self.direction
    def setRobotPosition(self, position):
        self.position = position
    def setRobotDirection(self, direction):
        self.direction = direction
    def updatePositionAndClean(self):
        raise NotImplementedError # don't change this!

class StandardRobot(Robot):
    def updatePositionAndClean(self):
        new_position = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_position):
            self.position = new_position
            self.room.cleanTileAtPosition(self.position)
        else:
            self.direction = random.randrange(0, 360)
            self.updatePositionAndClean()

class RandomWalkRobot(Robot):
    def updatePositionAndClean(self):
        new_position = self.position.getNewPosition(self.direction, self.speed)
        if self.room.isPositionInRoom(new_position):
            self.position = new_position
            self.room.cleanTileAtPosition(self.position)
            self.direction = random.randrange(0, 360)
        else:
            self.direction = random.randrange(0, 360)
            self.updatePositionAndClean()

def runSimulation(num_robots, speed, width, height, min_coverage, num_trials, robot_type):
    time_steps = 0
    for _ in range(num_trials):
        room = RectangularRoom(width, height)
        robots = [robot_type(room, speed) for _ in range(num_robots)]
        steps = 0
        while (room.getNumCleanedTiles() / room.getNumTiles()) < min_coverage:
            [r.updatePositionAndClean() for r in robots]
            steps += 1
        time_steps += steps
    return time_steps / num_trials