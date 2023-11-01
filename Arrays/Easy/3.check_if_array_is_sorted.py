a=[1,5,6,4,7]
n=len(a)
def sorted_or_not(arr,n):
    i=0
    j=n-1
    while i<j:
        if a[i]>a[i+1]:
            return False
        i+=1
    return True

print(sorted_or_not(a,n))