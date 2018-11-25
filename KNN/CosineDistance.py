import numpy as np
x = np.array([1,1])
y = np.array([4,5])

from math import *
def cos_distance(x,y):
    return np.dot(x,y)/(np.linalg.norm(x)*np.linalg.norm(y))

print(cos_distance(x,y))