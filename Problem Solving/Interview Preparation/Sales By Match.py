import os


def sock_merchant(array):
    """Return pairs of matching socks"""

    pairs = 0
    colors = set(array)
    counts = [array.count(c) for c in colors]
    for i in counts:
        if i == 1:
            counts.remove(1)
            pairs = [p//2 for p in counts]
        else:
            pairs = [p//2 for p in counts]

    return sum(pairs)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sock_merchant(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
