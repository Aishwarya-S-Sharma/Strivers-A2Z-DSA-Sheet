#If array has 1 peak
def find_peak(arr,n):
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    
    low,high=1,n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        elif arr[mid]>arr[mid+1]:
            high=mid-1

    return -1

#If array has multiple peaks
def find_peak(arr,n):
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    
    low,high=1,n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        elif arr[mid]>arr[mid+1]:
            high=mid-1
        else:
            low=mid+1

    return -1
#This can also be a solution for multiple peaks
#If array has 1 peak
def find_peak(arr,n):
    if n==1:
        return 0
    if arr[0]>arr[1]:
        return 0
    if arr[n-1]>arr[n-2]:
        return n-1
    
    low,high=1,n-2
    while low<=high:
        mid=(low+high)//2
        if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            return mid
        elif arr[mid]>arr[mid-1]:
            low=mid+1
        else:
            high=mid-1

    return -1

arr=list(map(int,input("Enter the list of numbers : ").split()))
print("The peak element is found at position : ",find_peak(arr,len(arr)))