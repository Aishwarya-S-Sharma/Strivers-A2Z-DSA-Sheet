def lower_bound(nums,n,target):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2            
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def upper_bound(nums,n,target):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2            
        if nums[mid]>target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def firstAndLast(arr, n, x): 
    lb=lower_bound(arr,n,x)
    ub=upper_bound(arr,n,x)
    if lb==n or arr[lb]!=x:
        return [-1]
    else:
        return [lb,ub-1]

nums=list(map(int,input("Enter the list of numbers : ").split()))
target=int(input("Enter the target number you need to search : "))
print("The floor and ceil is : ",firstAndLast(nums,len(nums),target))


#using pure binary search
def firstOccurrence(arr,n,k):
    i,j=0,n-1
    f=-1
    while i<=j:
        m=(i+j)//2
        if arr[m]==k:
            f=m
            j=m-1
        elif arr[m]<k:
            i=m+1
        else:
            j=m-1
    return f

def lastOccurrence(arr,n,k):
    i,j=0,n-1
    l=-1
    while i<=j:
        m=(i+j)//2
        if arr[m]==k:
            l=m
            i=m+1
        elif arr[m]<k:
            i=m+1
        else:
            j=m-1
    return l