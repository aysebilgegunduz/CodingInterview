
import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    for i in range(n):
        for j in range(n):
            if(j<n-i-1):
                print(" ", end='')
            else:
                print("#", end='')
        print("\n")
n=6
staircase(n)