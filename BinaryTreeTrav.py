class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.data = key


    def insertNode(self, data):
        if self.data:
            if self.data>data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insertNode(data)
            elif self.data<data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insertNode(data)
        else:
            self.data = data

    def printInOrder(self):
        if self.left:
            self.left.printInOrder()
        print(self.data)
        if self.right:
            self.right.printInOrder()


    def printPreOrder(self):
        print(self.data)
        if self.left:
            self.left.printPreOrder()
        if self.right:
            self.right.printPreOrder()

    def printPostOrder(self):
        if self.left:
            self.left.printPostOrder()
        if self.right:
            self.right.printPostOrder()
        print(self.data)

    def binarySearch(self, data):
        if self.data is None:
            return None
        elif self.data < data:
            return self.right.binarySearch(data)
        elif self.data > data:
            return self.left.binarySearch(data)
        elif self.data == data:
            return True

        return False



arr = [25,15,50,10,22,35,70,4,12,18,24,31,44,66,90]
arr = [20,15,27,19,10,1,12,35,30,50]
root = Node(arr[0])
for i in range(1,len(arr)):
    root.insertNode(arr[i])
print(root.binarySearch(35))