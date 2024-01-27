#Brute
# def median(matrix: [[int]], m: int, n: int) -> int:
#     a=[]
#     for i in range(m):
#         for j in range(n):
#             a.append(matrix[i][j])
#     a.sort()
#     return a[m*n//2]

 #Optimal
def upperBound(arr: [int], x: int, n: int) -> int:
    # Write your code here.
    l,h=0,n-1
    a=n
    while l<=h:
        m=(l+h)//2
        if arr[m]>x:
            a=m
            h=m-1
        else:
            l=m+1
    return a
    
def small_equal(mat,n,m,x):
    cnt=0
    for i in range(n):
        cnt+=upperBound(mat[i],x,m)
    return cnt

def median(matrix, m, n):
    low=float('inf')
    high=float('-inf')
    for i in range(m):
        low=min(low,matrix[i][0])
        high=max(high,matrix[i][n-1])
    req=(m*n)//2
    while low<=high:
        mid=(low+high)//2
        smallequal=small_equal(matrix,m,n,mid)
        if smallequal<=req:
            low=mid+1
        else:
            high=mid-1
    return low

n = 5
m = 5
mat = [[ 1, 5, 7, 9, 11 ],
      [ 2, 3, 4, 8, 9 ],
      [ 4, 11, 14, 19, 20 ],
      [ 6, 10, 22, 99, 100 ],
      [ 7, 15, 17, 24, 28 ]]
print("The matrix median is : ",median(mat,n,m))
