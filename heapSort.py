
def heapify(Arr, i , n):
    largest = i
    r = 2*i+2
    l = 2*i+1
    if(l<n and Arr[l]>Arr[i]):
        largest = l
    if(r<n and Arr[r]>Arr[largest]):
        largest = r
    if largest !=i:
        Arr[largest], Arr[i] = Arr[i], Arr[largest]
        heapify(Arr, largest, n)


def heapsort(Arr):
    n = len(Arr)

    for i in range(int(n/2)-1, -1, -1):
        heapify(Arr, i, n)

    for i in range(n-1, -1, -1):
        Arr[0], Arr[i] = Arr[i], Arr[0]
        heapify(Arr, 0, i)

Arr = [5,12,9,5,6,10]
T = Arr[0]
MyArr = Arr[1:]
print(MyArr)

heapsort(MyArr)
n = len(MyArr)
print("the result is: ")
counter = 1
print(MyArr)
for i in range(0,n):
    print(i)
    if counter >= 3:
        print(MyArr[i-2:i+1])
    else:
        print("-1")
    counter += 1
