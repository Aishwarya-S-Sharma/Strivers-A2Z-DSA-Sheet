def kthElement(a: [int], n1: int, b: [int], n2: int, k: int) -> int:
    left=k
    n=n1+n2
    if n1>n2:
        return kthElement(b,n2,a,n1,k)
    low=max(0,k-n2)
    high=min(k,n1)
    while low<=high:
        mid1=(low+high)//2
        mid2=left-mid1
        l1,l2=float('-inf'),float('-inf')
        r1,r2=float('inf'),float('inf')
        if mid1<n1:
            r1=a[mid1]
        if mid2<n2:
            r2=b[mid2]
        if mid1-1>=0:
            l1=a[mid1-1]
        if mid2-1>=0:
            l2=b[mid2-1]
        if l1<=r2 and l2<=r1:
            return max(l1,l2)
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
    return 0

array1 = [2, 3, 6, 7, 9]
array2 = [1, 4, 8, 10]
m = len(array1)
n = len(array2)
k = 5
print("The element at the kth position in the final sorted array is",kthElement(array1, array2, m, n, k))