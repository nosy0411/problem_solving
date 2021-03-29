import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):

    max_val=0
    
    dx=[-1,0,1,0,-1,0,1]
    dy=[-1,-1,-1,0,1,1,1]
    
    for y in range(1,5):
        for x in range(1,5):
            gls_sum=sum([arr[y+j][x+i] for i,j in zip(dx,dy)])

            if x==1 and y==1:
                max_val=gls_sum
                continue
            
            max_val=max(max_val,gls_sum)

    return max_val

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
