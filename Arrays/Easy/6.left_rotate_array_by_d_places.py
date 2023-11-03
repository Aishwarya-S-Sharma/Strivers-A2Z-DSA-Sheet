arr=[1,2,3,4,5,6,7]
k=3

#brute
n=len(arr)
k=k%n
temp=[0]*k
for i in range(k):
    temp[i]=arr[i]

for i in range(k,n):
    arr[i-k]=arr[i]

for i in range(n-k,n):
    arr[i]=temp[i-(n-k)]

print(arr)

#optimal
n=len(arr)
k=k%n
def twopt(arr,i,j):
    while i<j:
        arr[i],arr[j]=arr[j],arr[i]
        i+=1
        j-=1
    return arr
if k>0:
    twopt(arr,0,k-1)
    twopt(arr,k,n-1)
    twopt(arr,0,n-1)
print(arr)