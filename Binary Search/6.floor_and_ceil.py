def floor(nums,target):
    n=len(nums)
    low,high=0,n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]<=target:
            ans=nums[mid]
            low=mid+1
        else:
            high=mid-1
    return ans

def ceil(nums,target):
    n=len(nums)
    low,high=0,n-1
    ans=-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]>=target:
            ans=nums[mid]
            high=mid-1
        else:
            low=mid+1
    return ans

def floor_and_ceil(nums,target):
    f=floor(nums,target)
    c=ceil(nums,target)
    if f==-1 and c==-1:
        return [-1,-1]
    else:
        return [f,c]

nums=list(map(int,input("Enter the list of numbers : ").split()))
target=int(input("Enter the target number you need to search : "))
print("The floor and ceil is : ",floor_and_ceil(nums,target))