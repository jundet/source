import random

def randomzed_quicksort(A, p, r):
    if p < r:
        q = randomzed_(A, p, r)
        randomzed_quicksort(A, p, q-1)
        randomzed_quicksort(A, q+1, r)

def randomzed_(A, p, r):
    i = random.randint(p, r)
    A[r],A[i] = A[i],A[r]
    return partition(A, p, r)

def partition(A, p, r):
    x = A[r]
    i = p-1
    for j in range(p, r):
        if A[j]<=x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]
    return i+1

A = [5,6,9,4,10,2,3,7,1,8]
randomzed_quicksort(A, 0, len(A)-1)
print(A)
