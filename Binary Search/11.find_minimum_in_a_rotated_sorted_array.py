def min_in_a_rotated_sorted_array(arr,n):
    low,high,ans=0,n-1,float('inf')
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans

arr=list(map(int,input("Enter the list of numbers : ").split()))
print("The minimum element is : ",min_in_a_rotated_sorted_array(arr,len(arr)))

#optimization of above code
def min_in_a_rotated_sorted_array(arr,n):
    low,high,ans=0,n-1,float('inf')
    while low<=high:
        mid=(low+high)//2
        if arr[low]<=arr[high]:
            ans=min(ans,arr[low])
            break
        if arr[low]<=arr[mid]:
            ans=min(ans,arr[low])
            low=mid+1
        else:
            ans=min(ans,arr[mid])
            high=mid-1
    return ans