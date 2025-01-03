from collections import defaultdict

n, m = map(int, input().split())

A = [input(i).strip() for i in range(n)]
B = [input(i).strip() for i in range(m)]

result = defaultdict(list)

for char in B:
    inds = []
    for i, check in enumerate(A):
        if char in check:
            inds.append(i+1)
            continue
    result[char].extend(inds)

for k,v in result.items():
    if not v:
        result.update({k: [-1]})

for values in result.values():
    print(*values)
