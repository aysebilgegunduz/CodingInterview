#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    ar = s.split(":")
    if (ar[2][2] == 'P' and ar[0] != '12'):
        ar[0] = int(ar[0]) + 12
    elif (ar[0] == '12' and ar[2][2] == 'A'):
            ar[0] = "00"
    myStr = str(ar[0]) + ":"+ str(ar[1]) + ":"+ str(ar[2][0] + ar[2][1])
    print(myStr)
    return myStr

if __name__ == '__main__':

    s = "12:45:54PM"

    result = timeConversion(s)

    print(result)
