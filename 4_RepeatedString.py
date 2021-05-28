#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    if len(s)>=1 and len(s)<=100:
        if n >=1 and n<= (10**12):
            count = s.count('a')
            x = n % len(s)
            p = n//len(s)
            string=0
            char = ''
            string=count*p
            char+=s[0:x]  
            string +=char.count('a')   
            #string = string[:10]
            return string

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
