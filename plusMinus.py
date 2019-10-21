import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    pos = 0
    neg = 0
    for i in arr:
        if i >0:
            pos += 1
        elif i<0:
            neg += 1
    return [format(pos/len(arr), '.6f'), neg/len(arr), (len(arr)-pos-neg)/len(arr)]

if __name__ == '__main__':
    n = 6

    arr = [-4, 3, -9, 0, 4, 1]

    print(plusMinus(arr))
