import numpy as np
x = np.array([1,1])
y = np.array([4,5])

from math import *
def e_distance(x,y):
    return sqrt(sum(pow(a-b,2) for a,b in zip(x,y)))

print(e_distance(x,y))