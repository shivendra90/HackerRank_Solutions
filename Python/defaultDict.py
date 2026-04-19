# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int, input().split())

A = [input().strip() for _ in range(n)]
B = [input().strip() for _ in range(m)]

for char in B:
    inds = [index+1 for index, c in enumerate(A) if char == c]
    if char not in A:
        inds.append(-1)
    print(*inds)
