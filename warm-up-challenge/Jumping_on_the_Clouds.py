#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    i=0
    jump=0
    j=0

    while(i<len(c)-2):
        if c[i+j+1]==1:
            j+=1
        else:
            if j!=0:
                i+=(j+1)
                j=0
            else:
                if c[i+2]==1:
                    i+=1

                else:
                    i+=2

            jump+=1
    
    if i==len(c)-2:
        jump+=1                
    return jump




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()