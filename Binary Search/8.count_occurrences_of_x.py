def firstOccurrence(arr,n,k):
    low,high=0,n-1
    first=-1
    while low<=high:
        m=(low+high)//2
        if arr[m]==k:
            first=m
            high=m-1
        elif arr[m]<k:
            low=m+1
        else:
            high=m-1
    return first

def lastOccurrence(arr,n,k):
    low,high=0,n-1
    last=-1
    while low<=high:
        m=(low+high)//2
        if arr[m]==k:
            last=m
            low=m+1
        elif arr[m]<k:
            low=m+1
        else:
            high=m-1
    return last
def count_occurrences(arr, n, x): 
    lb=firstOccurrence(arr,n,x)
    ub=lastOccurrence(arr,n,x)
    if lb==-1 and ub==-1:
        return 0
    else:
        return ub-lb+1

nums=list(map(int,input("Enter the list of numbers : ").split()))
target=int(input("Enter the target number you need to search : "))
print("The occurrences of target is : ",count_occurrences(nums,len(nums),target))