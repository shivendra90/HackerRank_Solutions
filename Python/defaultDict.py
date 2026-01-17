from collections import defaultdict

n, m = map(int, input().split())

A = [input(i).strip() for i in range(n)]
B = [input(i).strip() for i in range(m)]

result = defaultdict(list)

for char in B:
    inds = [index+1 if char == c in B else -1 for index, c in enumerate(A)]
    print(*inds)

