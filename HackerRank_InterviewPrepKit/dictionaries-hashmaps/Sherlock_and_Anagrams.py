#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    
    num=0
    n=len(s)
    d=dict()
    for i in range(n):
        for j in range(i+1,n+1):
            key=''.join(sorted(s[i:j]))

            if key in d.keys():
                num+=d[key]
                d[key]=d[key]+1
            else:
                d[key]=1
    
    return num

            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()