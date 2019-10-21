#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    n=3
    t_arr = []
    for k in range(n+1):
        for l in range(n+1):
            result = 0
            for i in range(k, n+k):
                for j in range(l, n+l):
                    if not((i-k == 1 and j-l == 0 ) or (i-k==1 and j-l == 2 )):
                        result += arr[i][j]
            t_arr.append(result)
    t_arr.sort(reverse=True)

    return t_arr[0]
if __name__ == '__main__':

    arr = [[1,1,1,0,0,0],
           [0,1,0,0,0,0],
           [1,1,1,0,0,0],
           [0,0,2,4,4,0],
           [0,0,0,2,0,0],
           [0,0,1,2,4,0]]


    result = hourglassSum(arr)
    print(result)