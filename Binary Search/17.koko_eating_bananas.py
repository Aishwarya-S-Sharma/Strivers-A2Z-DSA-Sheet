from math import *
def calcTotalHour(piles,hourly):
    n=len(piles)
    totalH=0
    for i in range(n):
        totalH+=ceil(piles[i]/hourly)
    return totalH

def minEatingSpeed(piles,h):
    low,high=1,max(piles)
    while low<=high:
        mid=(low+high)//2
        totalH=calcTotalHour(piles,mid)
        if totalH<=h:
            high=mid-1
        else:
            low=mid+1
    return low

piles=list(map(int,input("Enter the values : ").split()))
h=int(input("Enter the hour : "))
print("The required number to finish all bananas within hour : ",minEatingSpeed(piles,h))