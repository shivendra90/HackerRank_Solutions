#!/bin/python3

import math
import os
import random
import re
import sys
import time

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#


def time_conversion(s):
    # Write your code here
    
    hms = s[:8]
    eve_morn = s[8:]
    form = "%H:%M:%S"

    hour = time.strptime(hms, form).tm_hour
    minutes = time.strptime(hms, form).tm_min
    sec = time.strptime(hms, form).tm_sec

    if hour == 12 and eve_morn == "AM":
        hour -= 12
    elif hour == 12 and eve_morn == "PM":
        hour = hour
    
    if hour < 10 and eve_morn == "AM":
        hour = f"0{hour}"
    elif hour != 12 and eve_morn == "PM":
        hour += 12
    
    if minutes < 10 and sec < 10:
        return f"{hour}:0{minutes}:0{sec}"
    elif minutes < 10:
        return f"{hour}:0{minutes}:{sec}"
    elif sec < 10:
        return f"{hour}:{minutes}:0{sec}"
    else:
        return f"{hour}:{minutes}:{sec}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = time_conversion(s)

    fptr.write(result + '\n')

    fptr.close()

print(time_conversion("12:01:01AM"))
