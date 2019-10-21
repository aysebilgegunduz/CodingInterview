def quicksort(A, l, r):
    i,j = partition(A, l, r)
    if l<j:
        quicksort(A, l, j)
    if r>i:
        quicksort(A, i, r)
    print(A)
def partition(A, l, r):
    pivot = A[int(l + ((r-l)/2))]
    i = l
    j = r
    while i<=j:
        while A[i]<pivot:
            i += 1
        while A[j]>pivot:
            j -= 1
        if i<=j:
            tmp = A[i]
            A[i] = A[j]
            A[j] = tmp
            i += 1
            j -= 1

    return i,j

A = [8, 7, 1, 2, 6, 9, 10, 3, 11]

quicksort(A, 0, len(A)-1)