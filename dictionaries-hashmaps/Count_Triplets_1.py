#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

import operator as op
from functools import reduce

def ncr(n, r):
    r = min(r, n-r)
    numer = reduce(op.mul, range(n, n-r, -1), 1)
    denom = reduce(op.mul, range(1, r+1), 1)
    return numer / denom

# Complete the countTriplets function below.
# 테스트 케이스 열라 까다로움. 111111 ~ 있는 경우랑 111111 10 10 10 10 1111 이런식으로 섞이면 progression만 고려해야함
# 전진방식으로는 답이 없음. 후진도 복잡해보임.
def countTriplets(arr, r):
    num=0

    d=Counter(arr)
    keys=d.keys()

    for key in keys:
                
        k=int(key)

        if (k in keys) and (r*k in keys) and (r*r*k in keys):
            if r==1 and d[k]>=3:
                num+=int(ncr(d[k],3))
            else:
                num+=d[k]*d[r*k]*d[r*r*k]

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
