def divide(A, l, r):
    if(l<r):
        middle = int(l + (r-l)/2)
        divide(A, l, middle)
        divide(A, middle+1, r)
        merge(A, middle, l, r)
    print(A)

def merge(A, m, l, r):
    n1 = m - l + 1
    n2 = r - m
    L = []
    R = []
    for i in range(0, n1):
        L.append(A[i+l])
    for i in range(0, n2):
        R.append(A[i+m+1])
    i=0
    j=0
    k=l
    while(i<n1 and j<n2):
        if L[i]<=R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
        k += 1
    while i<n1:
        A[k] = L[i]
        i += 1
        k += 1
    while j<n2:
        A[k] = R[j]
        j += 1
        k += 1

A = [8, 7, 1, 2, 6, 9, 10, 3, 11]

divide(A, 0, len(A)-1)
