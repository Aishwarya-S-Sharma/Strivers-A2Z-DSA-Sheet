def binary_search(nums,low,high,target):
    if low>high:  #base case
        return -1
    mid=(low+high)//2
    if nums[mid]==target:
        return mid
    elif nums[mid]>target:
        return binary_search(nums,low,mid-1,target)
    else:
        return binary_search(nums,mid+1,high,target)

nums=list(map(int,input("Enter the list of numbers : ").split()))
target=int(input("Enter the target number you need to search : "))
print("The target is found in : ",binary_search(nums,0,len(nums)-1,target))