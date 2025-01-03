n1 = int(input())

arr1 = set(map(int, input().split()))

n2 = int(input())

arr2 = set(map(int, input().split()))

diff = sorted(arr1.symmetric_difference(arr2))

for element in (diff):
    print(element)
