class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Node is defined as
    # self.left (the left child of the node)
    # self.right (the right child of the node)
    # self.info (the value of the node)

    def insert(self, val):
        # Enter you code here.
        node = self.root
        if node is None:
            node = Node(val)
            self.root = node
            return self.root
        while node is not None:
            if val > node.info:
                if node.right is not None:
                    node = node.right
                else:
                    node.right = Node(val)
                    return self.root
            if val < node.info:
                if node.left is not None:
                    node = node.left
                else:
                    node.left = Node(val)
                    return self.root


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.insert(arr[i])

preOrder(tree.root)
