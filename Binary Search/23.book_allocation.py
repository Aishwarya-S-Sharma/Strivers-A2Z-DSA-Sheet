#Brute Force
def fun(arr,pages):
    n=len(arr)
    stu=1
    pagesStudent=0
    for i in range(n):
        if pagesStudent+arr[i]<=pages:
            pagesStudent+=arr[i]
        else:
            stu+=1
            pagesStudent=arr[i]
    return stu
def findPages(arr,n,m):
    if m>n:
        return -1
    low=max(arr)
    high=sum(arr)
    for i in range(low,high+1):
        cnt_stu=fun(arr,i)
        if cnt_stu==m:
            return i
    return low

#Optimal
def fun(arr,pages):
    n=len(arr)
    stu=1
    pagesStudent=0
    for i in range(n):
        if pagesStudent+arr[i]<=pages:
            pagesStudent+=arr[i]
        else:
            stu+=1
            pagesStudent=arr[i]
    return stu
def findPages(arr: [int], n: int, m: int) -> int:
    if m>n:
        return -1
    low,high=max(arr),sum(arr)
    while low<=high:
        mid=(low+high)//2
        stu=fun(arr,mid)
        if stu>m:
            low=mid+1
        else:
            high=mid-1
    return low

book=list(map(int,input("Enter the pages of each book : ").split()))
m=int(input("Enter the number of students : "))
print("The answer is:",findPages(book,len(book),m))