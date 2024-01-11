def func(mid,n,m):
    ans=1
    for i in range(1,n+1):
        ans=ans*mid
        if ans>m:
            return 2
    if ans==m:
        return 1
    else:
        return 0
    
def NthRoot(n,m):
    l,h=1,m
    while l<=h:
        mid=(l+h)//2
        midN=func(mid,n,m)
        if midN==1:
            return mid
        elif midN==0:
            l=mid+1
        else:
            h=mid-1
    return -1

n=int(input("Enter the number for nth root : "))
m=int(input("Enter a number : "))
print("Nth root of a number : ",NthRoot(n,m))