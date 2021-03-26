#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the countTriplets function below.
def countTriplets(arr, r):
    num=0

    d2=Counter()
    d3=Counter()

    for i in arr:
        if i in d3:
            num+=d3[i]
        if i in d2:
            d3[i*r]+=d2[i]
        
        d2[i*r]+=1
    
    return num
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)

    fptr.write(str(ans) + '\n')

    fptr.close()
