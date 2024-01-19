#Brute
def countPartitions(arr,msum):
    n=len(arr)
    arr_s=0
    p=1
    for i in range(n):
        if arr_s+arr[i]<=msum:
            arr_s+=arr[i]
        else:
            p+=1
            arr_s=arr[i]
    return p


def largestSubarraySumMinimized(a, k):
    low=max(a)
    high=sum(a)
    for msum in range(low,high+1):
        if countPartitions(a,msum)==k:
            return msum
    return low

#Optimal
def countPartitions(arr,msum):
    n=len(arr)
    arr_s=0
    p=1
    for i in range(n):
        if arr_s+arr[i]<=msum:
            arr_s+=arr[i]
        else:
            p+=1
            arr_s=arr[i]
    return p


def largestSubarraySumMinimized(a, k):
    low=max(a)
    high=sum(a)
    while low<=high:
        mid=(low+high)//2
        partitions=countPartitions(a,mid)
        if partitions>k:
            low=mid+1
        else:
            high=mid-1
    return low

a=list(map(int,input("Enter the array elements : ").split()))
k=int(input("Enter the number of splits : "))
print("The answer is:",largestSubarraySumMinimized(a,k))