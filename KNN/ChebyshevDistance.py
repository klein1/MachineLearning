import numpy as np
x = np.array([1,1])
y = np.array([4,5])

from math import *
def q_distance(x,y):
    return abs(x-y).max()

print(q_distance(x,y))