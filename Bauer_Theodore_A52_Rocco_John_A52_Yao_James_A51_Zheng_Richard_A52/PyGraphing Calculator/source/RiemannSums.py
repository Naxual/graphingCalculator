# riemannSums.py

# Algorithm:
# 1. Take conditions (bounds, interval, number of rectangles, etc.) as input
# 2. Calculates Riemann sum for specified type of Riemann sum
#    (midpoint, left, right, trapezoidal) 

import numpy as np
import math
from scipy import integrate, misc


class RiemannSums:
    def __init__(self, conditions):
        self.__conditions = conditions

    def leftRiemann(self):
        sumRect = 0.0
        for i in range(self.__conditions[2]):
            X = self.__conditions[0] + i * self.__conditions[3]
            dX = abs(X - (self.__conditions[0] + (i+1) *
                          self.__conditions[3]))
            y = eval(self.__conditions[5])
            sumRect += (dX * y)
        return(sumRect)

    def rightRiemann(self):
        sumRect = 0.0
        for i in range(self.__conditions[2]):
            X = self.__conditions[0] + (i+1) * self.__conditions[3]
            dX = abs((self.__conditions[0] + i * self.__conditions[3])
                     - X)
            y = eval(self.__conditions[5])
            sumRect += (dX * y)
        return(sumRect)

    def midRiemann(self):
        sumRect = 0.0
        for i in range(self.__conditions[2]):
            X = self.__conditions[0] + (i+0.5) * self.__conditions[3]
            dX = abs((self.__conditions[0] + i * self.__conditions[3]) -
                     (self.__conditions[0] + (i+1) * self.__conditions[3]))
            y = eval(self.__conditions[5])
            sumRect += (dX * y)
        return(sumRect)

    def __str__(self):
        return str(self.__conditions)
