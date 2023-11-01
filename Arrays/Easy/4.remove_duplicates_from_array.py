a=[1,1,2,2,2,3,3]
n=len(a)
def remove_duplicates(a,n):
    i=0
    for j in range(1,n):
        if a[i]!=a[j]:
            i+=1
            a[i]=a[j]
    return i+1
print(remove_duplicates(a,n))