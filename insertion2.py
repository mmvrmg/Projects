def binSearch(A, n, first, last):
    if first == last:
        if A[first] > n:
            return first
        else:
            return first+1
        
    if first > last:
        return first
    
    mid = (first + last)//2
    
    if A[mid] < n:
        return binSearch(A, n, mid+1, last)
    elif A[mid] > n:
        return binSearch(A, n, first, mid-1)
    else:
        return mid
        
def insert(v, A, hi):
    for i in range (hi-1,-1,-1):
        print(A)
        j = binSearch(A, v, 0, i-1)
        A = A[:j] + [v] + A[j:i] + A[i+1:]
    return A

def insertionSort(A):
    for i in range(1,len(A)):
        insert(A[i],A,i)
    return A




list1 = [30,25,67,99,8,16,288,63,12,20]


print(insertionSort(list1))
