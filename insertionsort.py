def insertionSortC(A):
    A2 = [None] * len(A)
    A2[0] = A[0]
    for i in range(1,len(A)):
        insert(A[i], A2, i)
    return A2

def insert(v, A, hi):
    print(A)
    for i in range (hi-1,-1,-1):
        if v >= A[i]:
            A[i+1] = v
            return A
        A[i+1] = A[i]
    A[0] = v
    
list1 = [30,25,67,99,8,16,288,63,12,20]


print(insertionSortC(list1))
