#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'birthday' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER_ARRAY s
#  2. INTEGER d
#  3. INTEGER m
#

def birthday(s, d, m):
    """
    Returns the greatest sum of the array.
    Segments array as per parameter d and then finds
    number of times subarrays sum to m.
    """
    count = 0
    sums = []
    start, end = 0, m
    
    if len(s) < 2 and d == s:
        count = 1

    while end <= len(s):
        sums.append(sum(s[start:end]))
        start += 1
        end += 1
    
    for s in sums:
        if s == d:
            count += 1

    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
