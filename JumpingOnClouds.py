#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    # Write your code here
    if len(c) >= 2 and len(c)<= 100:
        if c[0]==0 and c[len(c)-1]==0:
            jc=0
            lst = []
            i=0
            while(i<len(c)):
                if i < len(c)-2 and c[i+2] !=1 :
                    jc += 1
                    i+=2
                else:
                    jc += 1
                    i+=1
                if i >= len(c)-1:
                    break

                    
            return jc
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
