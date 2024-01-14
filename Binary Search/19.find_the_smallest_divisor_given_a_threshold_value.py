from math import *
#Brute Force
def smallestDivisor(arr, limit):
    n=len(arr)
    for i in range(1,max(arr)):
        s=0
        for j in range(n):
            s+=ceil(arr[j]/i)
        if s<=limit:
            return i
    return -1


#Optimal: Binary search on answers
def sumofD(arr,div):
    s=0
    for i in range(len(arr)):
        s+=ceil(arr[i]/div)
    return s
def smallestDivisor(arr, limit):
    low,high=1,max(arr)
    while low<=high:
        mid=(low+high)//2
        if sumofD(arr,mid)<=limit:
            high=mid-1
        else:
            low=mid+1
    return low