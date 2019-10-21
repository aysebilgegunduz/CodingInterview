import random
import math
myRand = []

"""
for i in range(_size):
    myRand.append(random.randint(0,10))
j = _size - 1
a = 1
print(myRand)
"""
""" GREEDY """
"""
j = _size - 1
a = 1
print(myRand)
while (j != 0):
    for i in range(j):
        _temp = myRand[i] + myRand[j]
        if(_temp == _sum):
            print("YES")
            a = 0
    j = j - 1


if(a == 1):
    print("No!!!")
"""

""" BINARY SEARCH """
def binaryTree( myRand, last, first, _temp):

    if(first<=last):
        mid = int(first+ (last - first) / 2)
        if(myRand[mid] == _temp):
            return myRand[mid]
        elif _temp < myRand[mid]:
            return binaryTree(myRand,  mid-1,first, _temp)
        else:
            return binaryTree(myRand, last, mid+1, _temp)
    return -1


def lowHighMove(myRand, _size, _sum):
    """
    Linear movement [1,2,4,4] start with l and r sum and check whether it's the summation you're looking for
    if smaller move left index to right way otherwise vise versa
    :param myRand: array
    :param _size: array lenght
    :param _sum: sum I look for
    :return: true or false
    """
    first = 0
    last = _size-1
    while(first<last):
        _temp = myRand[first] + myRand[last]
        if(_temp == _sum):
            return True
        elif(_temp < _sum):
            first += 1
        else:
            last -= 1
    return False
_size = 4
_sum = 8
myRand = [2, 4, 4, 5]
counter = 0

def hasPairWithSum(myRand, _sum):
    """
    If it's not sorted
    :param myRand:
    :param _size:
    :param _sum:
    :return:
    """
    _hset = set()
    for i in myRand:
        print(i)
        if ( i in _hset):
            return True
        _hset.add(_sum-i)

    return False
"""
for i in range(_size-1):
    _temp = _sum - myRand[i]
    print("temp: ", _temp)
    if(binaryTree(myRand,  len(myRand) - 1,i+1, _temp) == _temp):
        print("YEEEES!!!!")
        break
    else:
        counter += 1
if counter == 3:
    print("NOOOOO!!!!")
"""
"""
if(lowHighMove(myRand, _size, _sum)):
    print("YEEEES!!!!")
else:
    print("NOOOOO!!!!")
"""

print(hasPairWithSum(myRand,_sum))