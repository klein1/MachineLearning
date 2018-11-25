import numpy as np
x = np.array([1,1])
y = np.array([4,5])

from math import *
def m_distance(x,y):
    return sum(abs(x-y))

print(m_distance(x,y))