#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):

    d=[0]*(n+1)
    max_val=0
    for query in queries:
        d[query[0]-1]+=query[2]
        d[query[1]]+=query[2]*(-1)
    
    max_dif=0

    for i in d:
        max_dif+=i
        
        if max_val<max_dif:
            max_val=max_dif

    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()