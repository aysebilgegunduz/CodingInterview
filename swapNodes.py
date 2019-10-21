#!/bin/python3

import os
import sys
sys.setrecursionlimit(15000)


class Node:
    def __init__(self, info, d):
        self.left = None
        self.right = None
        self.data = info
        self.depth = d

    def __str__(self):
        return str(self.data)


class BinaryTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        to_visit = []
        if self.root is None:
            self.root = Node(1, 0)
        current = self.root
        to_visit.append(current)

        while len(to_visit):
            current = to_visit.pop(0)
            if not(current.left) and current.data != -1:
                current.left = Node(val, current.depth+1)
                break
            elif current.left.data != -1:
                to_visit.append(current.left)
            if not(current.right) and current.data != -1:
                current.right = Node(val, current.depth+1)
                break
            elif current.right.data != -1:
                to_visit.append(current.right)



#
# Complete the swapNodes function below.
#


def createArray(root):
    current = root
    to_visit = []
    result = []
    while True:
        if current is not None and current.data != -1:
            to_visit.append(current)
            current = current.left
        elif to_visit:
            current = to_visit.pop()
            result.append(current.data)
            current = current.right
        else:
            break
    return result


def swapEveryKLevelUtil(root, level, k):
    # Base Case
    if (root is None or (root.left is None and
                         root.right is None)):
        return

        # If current level+1 is present in swap vector
    # then we swap left and right node
    if (level + 1) % k == 0:
        root.left, root.right = root.right, root.left

        # Recur for left and right subtree
    swapEveryKLevelUtil(root.left, level + 1, k)
    swapEveryKLevelUtil(root.right, level + 1, k)

def swapNodes(indexes, queries):
    to_visit = []
    tree = BinaryTree()
    result = []
    for i in range(len(indexes)):
        for j in range(len(indexes[i])):
                tree.create(indexes[i][j])
    for i in range(len(queries)):
        swapEveryKLevelUtil(tree.root, 0, queries[i])
        result.append(createArray(tree.root))

    return result


if __name__ == '__main__':

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)
    print(result)

