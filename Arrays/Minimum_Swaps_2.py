#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swap=0
    for i in range(len(arr)):
        if arr[i]==i+1:
            continue
        else:
            while(arr[i]!=(i+1)):
                temp=arr[arr[i]-1]
                arr[arr[i]-1]=arr[i]
                arr[i]=temp
                swap+=1
        
    
    return swap

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()