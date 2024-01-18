#Brute force

def finddays(weights,capacity):
    n=len(weights)
    load=0
    day=1
    for i in range(n):
        if load+weights[i]>capacity:
            day=day+1
            load=weights[i]
        else:
            load+=weights[i]
    return day
def leastWeightCapacity(weights, d):
    for capacity in range(max(weights),sum(weights)+1):
        if finddays(weights,capacity)<=d:
            return capacity
    return -1


#optimal
def finddays(weights,capacity):
    n=len(weights)
    load=0
    day=1
    for i in range(n):
        if load+weights[i]>capacity:
            day=day+1
            load=weights[i]
        else:
            load+=weights[i]
    return day
def leastWeightCapacity(weights, d):
    low,high=max(weights),sum(weights)
    while low<=high:
        mid=(low+high)//2
        if finddays(weights,mid)<=d:
            high=mid-1
        else:
            low=mid+1
    return low
weights=list(map(int,input("Enter the weights: ").split()))
d=int(input("Enter the days : "))
print("The least capacity is : ",leastWeightCapacity(weights,d))