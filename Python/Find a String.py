def count_substring(a, b):
    """Returns number of times a substring repeats."""
    a = str(a)
    b = str(b)

    times = 0
    i = 0
    while i != len(a):
        if b in a[i:len(b)+i]:
            times += 1
        i += 1

    return times


