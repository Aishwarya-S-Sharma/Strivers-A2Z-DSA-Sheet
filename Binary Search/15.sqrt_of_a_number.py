#any of the three works
def sqrt(n):
    low,high=1,n
    ans=1
    while low<=high:
        mid=(low+high)//2
        if mid*mid<=n:
            ans=mid
            low=mid+1
        else:
            high=mid-1
    return ans

def sqrt(n):
    low,high=1,n
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            low=mid+1
        else:
            high=mid-1
    return high

def sqrt(n):
    low,high=1,n//2
    while low<=high:
        mid=(low+high)//2
        if mid*mid==n:
            return mid
        elif mid*mid<n:
            low=mid+1
        else:
            high=mid-1
    return high



n=int(input("Enter a number : "))
print("The sqrt of a number is : ",sqrt(n))