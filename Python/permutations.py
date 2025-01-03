from itertools import permutations

string = str(input()).upper()

string = string.split()

perm = sorted(list(permutations(string[0], int(string[1]))))

for p in perm:
    print(''.join(p))
