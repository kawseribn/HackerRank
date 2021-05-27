#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglassSum(arr):
    # Write your code here
    if len(arr)<=6 and len(arr[0])<=6:
        hour = 0
        hourglass=[]
        i=0
        while (i<len(arr)-2):
            if hour>=16:
              return max(hourglass)
            count = 0
            j=0
            while (j<len(arr[0])-2):
                    a = arr[i][j]
                    b = arr[i][j+1]
                    c = arr[i][j+2]
                    d = arr[i+1][j+1]
                    e = arr[i+2][j]
                    f = arr[i+2][j+1]
                    g = arr[i+2][j+2]
                    hourglass.append(a+b+c+d+e+f+g)
                    j+=1
            hour+=1
            i+=1
        #print(hourglass)
        return max(hourglass)
                        
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
