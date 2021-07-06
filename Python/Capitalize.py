import os
import sys

def solve(s):
    """
    Returns capitalized first alphabets only.
    """
    stripped = s.strip().split(' ')
    caps = [x.capitalize() for x in stripped]
    
    return str(' '.join(caps))


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
