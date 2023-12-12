import numpy as np
import math

def distance(store1, store2):
    return (math.sqrt(pow(store1[0] - store2[0], 2) + pow(store1[1] - store2[1], 2)))

def closest(coordinates):
    shortest = 10000000000
    for i in range(len(coordinates) - 1):
        for j in range(len(coordinates)):
            if (i != j and shortest >= distance(coordinates[i], coordinates[j])):
                shortest = distance(coordinates[i], coordinates[j])
    return (shortest)

coordinates = [(1, 9), (2, 100), (35, 70), (12, 80), (75, 6), (20, 93)]
print(closest(coordinates))