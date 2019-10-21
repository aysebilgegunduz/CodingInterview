import math
import os
import random
import re
import sys

def dynamicArray(n, queries):
    # Write your code here
    lastInteger = 0
    seqlist = []
    for i in range(n):
        seqlist.append([])
    for i in range(len(queries)):
        if(queries[i][0] == 1):
            x = (queries[i][1]^lastInteger)%n
            seqlist[x].append(queries[i][2])
        elif(queries[i][0] == 2):
            x = (queries[i][1]^lastInteger)%n
            y = seqlist[x][queries[i][2]%len(seqlist[x])]
            lastInteger = y
            print(lastInteger)



if __name__ == '__main__':

    n=2
    q=5

    queries = [[1,0,5],
           [1,1,7],
           [1,0,3],
           [2,1,0],
           [2,1,1]]

    result = dynamicArray(n, queries)