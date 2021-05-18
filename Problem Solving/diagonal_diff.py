n = int(input())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))


def diagonalDifference(arr):
    """
    Return the asbolute difference
    of left and right diagonal elements.
    """
    