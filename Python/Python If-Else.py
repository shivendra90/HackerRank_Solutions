 
#!/bin/python3

import math
import os
import random
import re
import sys


if __name__ == '__main__':
    n = int(input().strip())

    while n <= 100:
        if n % 2 == 0:
            if 2 <= n <= 5:
                print("Not Weird")
                break
        else:
            print("Weird")
            break
        if n % 2 == 0:
            if 6 <= n <= 20:
                print("Weird")
                break
        else:
            print("Not Weird")
            break
        if n % 2 == 0:
            if n > 20:
                print("Not Weird")
                break
        else:
            print("Weird")
            break

