def divide_substring(inp, k):
    if k == 1:
        for c in inp:
            print(c)
    else:
        constant = k
        start = 0
        out = []
        for ind in range(start, k):
            out.append(inp[start:k])
            start += constant
            k += constant

    # print each iterable 
        for string in out:
            print(''.join(dict.fromkeys(string)))

divide_substring('qwertyuiop', 1)
