from collections import Counter

n_shoe = int(input())
shoe_sizes = Counter([int(x) for x in input().split()])
n_customers = int(input())
total = 0

for cust in range(n_customers):
    size_price = [int(y) for y in input().split()]
    if size_price[0] in shoe_sizes.keys():
        total += size_price[1]
        shoe_sizes[size_price[0]] -= 1
        if shoe_sizes[size_price[0]] == 0:
            shoe_sizes.pop(size_price[0])

print(total)
