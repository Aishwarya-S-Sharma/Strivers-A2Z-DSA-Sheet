def min_in_a_rotated_sorted_array(arr,n):
    low,high,ans=0,n-1,float('inf')
    index=-1
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            break
        if arr[low]<=arr[mid]:
            if arr[low]<ans:
                index=low
                ans=arr[low]
            low=mid+1
        else:
            high=mid-1
            if arr[mid]<ans:
                index=mid
                ans=arr[mid]
    return index

arr=list(map(int,input("Enter the list of numbers : ").split()))
print("The array has been rotated for : ",min_in_a_rotated_sorted_array(arr,len(arr)), "times")