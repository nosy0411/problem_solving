#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):

    bribe=0
    i=len(q)-2
    
    while(1):

        if (q[i]-(i+1))>=3:
            print("Too chaotic")
            break

        else:
            if i==len(q)-2:
                if q[i+1]<q[i]:
                    bribe+=1
                    temp=q[i+1]
                    q[i+1]=q[i]
                    q[i]=temp


            else:
                if q[i+2]<q[i]:
                    bribe+=2
                    temp=q[i]
                    q[i]=q[i+1]
                    q[i+1]=q[i+2]
                    q[i+2]=temp

                elif q[i+1]<q[i]:
                    bribe+=1
                    temp=q[i+1]
                    q[i+1]=q[i]
                    q[i]=temp
        
        i-=1
        if i==-1:
            print(bribe)
            break


if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
