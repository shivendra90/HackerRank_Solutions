def dynamicArray(n, queries):
    # Write your code here
    lastAnswer = 0
    arr = [[] for _ in range(n)]
    final = []
    
    for q in queries:
        x = q[1]
        if q[0] == 1:
            idx = ((x ^ lastAnswer) % n)
            arr[idx].append(q[2])
        elif q[0] == 2:
            idx = ((x ^ lastAnswer) % n)
            lastAnswer = arr[idx][q[2] % len(arr[idx])]
            final.append(lastAnswer)

    return final


if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    print('\n'.join(map(str, result)))
    print('\n')

