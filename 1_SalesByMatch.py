#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    if n<=100 and n>=1:
        count_p = 0
        checked =[]
        for i in range(len(ar)):
            if ar[i]>=1 and ar[i]<=100:
                if ar[i] not in checked:
                    checked.append(ar[i])
                    count_p+=(int(ar.count(ar[i])/2))
        return count_p
    else:
        return 0
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
