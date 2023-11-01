a=[1,2,3,4,5,6]
n=len(a)
#brute
def rotate_arr(a,n):
    temp=[0]*n
    for i in range(1,n):
        temp[i-1]=a[i]
    temp[n-1]=a[0]
    for i in range(n):
        print(temp[i],end=' ')
print(rotate_arr(a,n))


#optimal
def rotate_arr(a,n):
    temp=a[0]
    for i in range(n-1):
        a[i]=a[i+1]
    a[n-1]=temp
    for i in range(n):
        print(a[i],end=' ')
print(rotate_arr(a,n))

