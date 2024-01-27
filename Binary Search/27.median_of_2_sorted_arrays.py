#Brute
def median(a: int, b: int) -> float:
    n1=len(a)
    n2=len(b)
    c=[]
    i,j=0,0
    while i<n1 and j<n2:
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        else:
            c.append(b[j])
            j+=1
    c.extend(a[i:])
    c.extend(b[j:])
    
    n=n1+n2
    if n%2==1:
        return float(c[n//2])
    else:
        return ((c[n//2]+c[n//2-1])/2.0)


#Better
def median(a: int, b: int) -> float:
    n1=len(a)
    n2=len(b)
    n=n1+n2
    ind2=n//2
    ind1=ind2-1
    cnt=0
    i,j=0,0
    ind1el=-1
    ind2el=-1
    while i<n1 and j<n2:
        if a[i]<b[j]:
            if cnt==ind1:ind1el=a[i]
            if cnt==ind2:ind2el=a[i]
            cnt+=1
            i+=1
        else:
            if cnt==ind1:ind1el=b[j]
            if cnt==ind2:ind2el=b[j]
            cnt+=1
            j+=1

    while i<n1:
        if cnt==ind1:ind1el=a[i]
        if cnt==ind2:ind2el=a[i]
        cnt+=1
        i+=1
    
    while j<n2:
        if cnt==ind1:ind1el=b[j]
        if cnt==ind2:ind2el=b[j]
        cnt+=1
        j+=1

    if n%2==1:
        return float(ind2el)

    else:
        return (ind1el+ind2el)/2.0

#Optimal
def median(a: int, b: int) -> float:
    n1=len(a)
    n2=len(b)
    left=(n1+n2+1)//2
    n=n1+n2
    if n1>n2:
        return median(b,a)
    low=0
    high=n1
    while low<=high:
        mid1=(low+high)//2
        mid2=left-mid1
        l1,l2=float('-inf'),float('-inf')
        r1,r2=float('inf'),float('inf')
        if mid1<n1:
            r1=a[mid1]
        if mid2<n2:
            r2=b[mid2]
        if mid1-1>=0:
            l1=a[mid1-1]
        if mid2-1>=0:
            l2=b[mid2-1]
        if l1<=r2 and l2<=r1:
            if n%2==1 :
                return float(max(l1,l2))
            else:
                return (max(l1,l2)+min(r1,r2))/2.0
        elif l1>r2:
            high=mid1-1
        else:
            low=mid1+1
    return 0

a = [1, 4, 7, 10, 12]
b = [2, 3, 6, 15]
print("The median of two sorted arrays is", "{:.1f}".format(median(a, b)))