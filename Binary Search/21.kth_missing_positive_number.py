#Brute Force
def missingK(vec, n, k):
    for i in range(n):
        if vec[i]<=k:
            k+=1
        else:
            break
    return k

#Optimal
def missingK(vec, n, k):
    low,high=0,n-1
    while low<=high:
        mid=(low+high)//2
        missing=vec[mid]-(mid+1)
        if missing<k:
            low=mid+1
        else:
            high=mid-1
    return low+k
vec=list(map(int,input("Enter the numbers : ").split()))
k=int(input("Enter the value of k : "))
print("The kth missing number is : ",missingK(vec,len(vec),k))