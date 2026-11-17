def birthday(s, d, m):
    """
    Returns the greatest sum of the array.
    Segments array as per parameter d and then finds
    number of times subarrays sum to m.
    """
    count = 0
    sums = []
    start, end = 0, m
    
    if len(s) < 2 and d == s:
        count = 1

    while end <= len(s):
        sums.append(sum(s[start:end]))
        start += 1
        end += 1
    
    for s in sums:
        if s == d:
            count += 1

    return count


arr1 = [1,2,1,3,2]
d, m = 3, 2
print(birthday(arr1, d, m))

arr2 = [1,1,1,1,1,1]
print(birthday(arr2, d, m))

arr3 = [2, 5, 1, 3, 4, 4, 3, 5, 1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1]
print(birthday(arr3, 18, 7))
