# 归并排序，分-治

# 分
def sort(A):
    if len(A)<=1:
        return A

    middle = len(A)//2
    left = sort(A[:middle])
    right = sort(A[middle:])
    # 治
    return merge(left,right)

# 治
def merge(left,right):
    c = []
    h = j = 0
    while j<len(left) and h<len(right):
        if left[j]<right[h]:
            c.append(left[j])
            j+=1
        else:
            c.append(right[h])
            h+=1

    if j==len(left):
        for i in right[h:]:
            c.append(i)
    if h==len(right):
        for i in left[j:]:
            c.append(i)

    return c

X = [2,3,7,4,6,9,1,5,8]
print(sort(X))
