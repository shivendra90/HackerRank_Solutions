#!/bin/python3

import os
import sys

#
# Complete the 'findSum' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY numbers
#  2. 2D_INTEGER_ARRAY queries
#

def findSum(numbers, queries):
    """
    Given numbers (list of ints) and queries (list of [L, R, optional add_if_zero]),
    return a list of sums for each query (inclusive). If any value in numbers[L-1:R]
    is zero, add add_if_zero (0 if missing) to that query's result.
    """
    n = len(numbers)
    # prefix sums for ranges
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + numbers[i]
    # prefix count of zeros for O(1) zero-check in a range
    zero_prefix = [0] * (n + 1)
    for i in range(n):
        zero_prefix[i+1] = zero_prefix[i] + (1 if numbers[i] == 0 else 0)

    result = []
    for q in queries:
        if not q or len(q) < 2:
            result.append(0)
            continue
        l, r = q[0], q[1]
        add_if_zero = q[2] if len(q) > 2 else 0
        # clamp to valid 1-based bounds
        if l < 1:
            l = 1
        if r > n:
            r = n
        if l > r:
            result.append(0)
            continue
        s = prefix[r] - prefix[l-1]
        zeros_in_range = zero_prefix[r] - zero_prefix[l-1]
        if zeros_in_range > 0:
            s += add_if_zero
        result.append(s)
    return result


if __name__ == '__main__':
    output_path = os.environ.get('OUTPUT_PATH')
    if output_path:
        fptr = open(output_path, 'w')
    else:
        fptr = sys.stdout

    numbers_count = int(input().strip())

    numbers = []

    for _ in range(numbers_count):
        numbers_item = int(input().strip())
        numbers.append(numbers_item)

    queries_rows = int(input().strip())
    queries_columns = int(input().strip())

    queries = []

    for _ in range(queries_rows):
        queries.append(list(map(int, input().rstrip().split())))

    result = findSum(numbers, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    # only close when we opened a file
    if output_path:
        fptr.close()
