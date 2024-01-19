#Brute
def countPainters(boards,time):
    n=len(boards)
    painters=1
    a=0
    for i in range(n):
        if a+boards[i]<=time:
            a+=boards[i]
        else:
            painters+=1
            a=boards[i]
    return painters

def findLargestMinDistance(boards,k):
    low,high=max(boards),sum(boards)
    for time in range(low,high+1):
        if countPainters(boards,time)<=k:
            return time
    return low

#optimal
def countPainters(boards,time):
    n=len(boards)
    painters=1
    a=0
    for i in range(n):
        if a+boards[i]<=time:
            a+=boards[i]
        else:
            painters+=1
            a=boards[i]
    return painters

def findLargestMinDistance(boards,k):
    low,high=max(boards),sum(boards)
    while low<=high:
        mid=(low+high)//2
        if countPainters(boards,mid)>k:
            low=mid+1
        else:
            high=mid-1
    return low

boards=list(map(int,input("Enter the board elements : ").split()))
k=int(input("Enter the number of painters: "))
print("The answer is:",findLargestMinDistance(boards,k))