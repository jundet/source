# 插入排序

def insertion_sort(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]>key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

def insertion_sort_down(A):
    for j in range(1,len(A)):
        key = A[j]
        i = j-1
        while i>-1 and A[i]<key:
            A[i+1] = A[i]
            i -= 1
        A[i+1] = key
    return A

X = [2,3,7,4,6,9,1,5,8]
print(insertion_sort(X))
print(insertion_sort_down(X))

