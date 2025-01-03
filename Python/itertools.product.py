
list_1 = [int(x) for x in input().split()]
list_2 = [int(y) for y in input().split()]

prod = []

for x in list_1:
    for y in list_2:
        prod.append((x, y))

for element in prod:
    print(element, end='\n')
