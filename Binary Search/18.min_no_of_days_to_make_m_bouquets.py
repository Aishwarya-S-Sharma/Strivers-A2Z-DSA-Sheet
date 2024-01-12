#Brute force
def possible(arr,m,k,day):
    cnt=0
    noOfb=0
    n=len(arr)
    for i in range(n):
        if arr[i]<=day:
            cnt+=1
        else:
            noOfb+=cnt//k
            cnt=0
    noOfb+=cnt//k
    return  noOfb>=m

def roseGarden(arr,m,k):
    for i in range(min(arr),max(arr)+1):
        if possible(arr,m,k,i):
            return i
    return -1

#Optimal
def possible(arr,m,k,day):
    cnt=0
    noOfb=0
    n=len(arr)
    for i in range(n):
        if arr[i]<=day:
            cnt+=1
        else:
            noOfb+=cnt//k
            cnt=0
    noOfb+=cnt//k
    return  noOfb>=m
def min_day(arr,m,k):
    n=len(arr)
    if m*k>n:
        return -1
    low,high=min(arr),max(arr)
    while low<=high:
        mid=(low+high)//2
        if possible(arr,m,k,mid):
            high=mid-1
        else:
            low=mid+1
    return low

bloomDay=list(map(int,input("Enter the bloom days: ").split()))
m=int(input("Enter no. of bouquets to make : "))
k=int(input("Enter no. adjacent flowers to take : "))
print("The minimum days required to make m bouquets is : ",min_day(bloomDay,m,k))