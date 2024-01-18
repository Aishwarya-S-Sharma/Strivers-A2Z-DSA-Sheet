#Brute force
def canPlace(stalls,dist,k):
    cnt_cow=1
    last=stalls[0]
    n=len(stalls)
    for i in range(1,n):
        if stalls[i]-last>=dist:
            cnt_cow+=1
            last=stalls[i]
    if cnt_cow>=k:
        return True
    else:
        return False
def aggressiveCows(stalls, k):
    n=len(stalls)
    stalls.sort()
    limit=max(stalls)-min(stalls)
    for i in range(1,limit+1):
        if canPlace(stalls,i,k)==True:
            continue
        else:
            return i-1
    return limit

stalls=list(map(int,input("Enter the stalls : ").split()))
k=int(input("Enter the number of cows : "))
print("The maximum possible minimum distance is:",aggressiveCows(stalls,k))