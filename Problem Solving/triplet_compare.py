import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.


def compareTriplets(a, b):
    
    score = [0, 0]
    try:
        for alice, bob in zip(a, b):
            if alice > bob:
                score[0] += 1
            elif alice < bob:
                score[1] += 1
        return score
    
    except TypeError:
        print("One or more inputs is not a list.")



a = "A"
b = [1, 2, 3]

print(compareTriplets(a, b))
