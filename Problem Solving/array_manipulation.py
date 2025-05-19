from collections import deque

first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

queries = []

for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))


def arrayManipulation(n, queries):
    # Write your code here
    arr = deque([0] * n)

    for q in queries:
        a, b, k = (q[0]-1, q[1], q[2])
        arr[a] += k
        if b < n:
            arr[b] -= k

    curr, max_v = 0, 0
    for val in arr:
        curr += val
        if curr > max_v:
            max_v = curr

    return max_v

result = arrayManipulation(n, queries)
print(result)
