#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the freqQuery function below.
def freqQuery(queries):
    ans=[]
    d=Counter()

    for query in queries:
        if query[0]==1:
            d[query[1]]+=1

        elif query[0]==2:
            if query[1] in d and d[query[1]]>0:
                d[query[1]]-=1
        else:
            check=0
            for val in set(d.values()):
                if val==query[1]:
                    ans.append(1)
                    check=1
                    break
            if check==0:
                ans.append(0)        

    return ans
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
