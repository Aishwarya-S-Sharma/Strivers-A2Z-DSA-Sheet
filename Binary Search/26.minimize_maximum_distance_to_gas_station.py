#Brute
def minimiseMaxDistance(arr: [int], k: int) -> float:
    n=len(arr)
    Howmany=[0]*(n-1)
    for gasStation in range(1,k+1):
        maxSection,maxInd=-1,-1
        for i in range(n-1):
            diff=arr[i+1]-arr[i]
            sectionLength=diff/(Howmany[i]+1)
            if maxSection<sectionLength:
                maxSection=sectionLength
                maxInd=i
        Howmany[maxInd]+=1

    maxAns=-1
    for i in range(n-1):
        diff=arr[i+1]-arr[i]
        sectionLength=diff/(Howmany[i]+1)
        maxAns=max(maxAns,sectionLength)
    return maxAns

#Better
import heapq
def minimiseMaxDistance(arr: [int], k: int) -> float:
    n=len(arr)
    Howmany=[0]*(n-1)
    pq=[]
    for i in range(n-1):
        heapq.heappush(pq,((-1)*(arr[i+1]-arr[i]),i))
    for gasStation in range(1,k+1):
        tp=heapq.heappop(pq)
        sectionInd=tp[1]
        Howmany[sectionInd]+=1

        iniDiff=arr[sectionInd+1]-arr[sectionInd]
        newSection=iniDiff/(Howmany[sectionInd]+1)
        heapq.heappush(pq,(newSection*(-1),sectionInd))
    return pq[0][0]*(-1)
        

#Optimal
def noOfGasStations(arr,dist):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(1, n):
        numberInBetween = ((arr[i] - arr[i - 1]) / dist)
        if (arr[i] - arr[i - 1]) == (dist * numberInBetween):
            numberInBetween -= 1
        cnt += numberInBetween
    return cnt
def minimiseMaxDistance(arr: [int], k: int) -> float:
    n = len(arr)  # size of the array
    low = 0
    high = 0
    for i in range(n - 1):
        high = max(high,abs(arr[i + 1] - arr[i]))
    diff = 1e-7
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = noOfGasStations(arr,mid)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high
        
        #or

def noOfGasStations(arr,dist):
    n = len(arr)  # size of the array
    cnt = 0
    for i in range(n-1):
        numberInBetween =arr[i+1]-arr[i]
        cnt += numberInBetween//dist
    return cnt
def minimiseMaxDistance(arr: [int], k: int) -> float:
    n = len(arr)  # size of the array
    low = 0
    high = 0
    for i in range(n - 1):
        high = max(high,abs(arr[i + 1] - arr[i]))
    diff = 1e-7
    while high - low > diff:
        mid = (low + high) / 2.0
        cnt = noOfGasStations(arr,mid)
        if cnt > k:
            low = mid
        else:
            high = mid

    return high
        
arr=list(map(int,input("Enter the array elements : ").split()))
k=int(input("Enter the number of gas station to place: "))
print("The answer is:",minimiseMaxDistance(arr,k))
