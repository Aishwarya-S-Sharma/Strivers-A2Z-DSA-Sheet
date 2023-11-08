#brute1
def longest_sub_array(a,k):
    max_length=0
    n=len(a)
    for i in range(n):
        for j in range(n):
            s=0
            for K in range(i,j+1):
                s+=a[K]
            if s==k:
                max_length=max(max_length,j-i+1)
    return max_length

#brute2
def longest_sub_array(a,k):
    max_length=0
    n=len(a)
    for i in range(n):
        s=0
        for j in range(n):
            s+=a[j]
            if s==k:
                max_length=max(max_length,j-i+1)
    return max_length

#better
def longest_sub_array(a,k):
    m={}
    s=0
    max_length=0
    n=len(a)
    for i in range(n):
        s+=a[i]
        if s==k:
            max_length=max(max_length,i+1)
        rem=s-k
        if rem in m:
            length=i-m[rem]
            max_length=max(max_length,length)
        if s not in m:
            m[s]=i
    return max_length

#optimal
def longest_sub_array(a,k):
    max_length=0
    n=len(a)
    s=a[0]
    left,right=0,0
    while right<n:
        while left<=right and s>k:
            s-=a[left]
            left+=1
        if s==k:
            max_length=max(max_length,right-left+1)
        right+=1
        if right<n:
            s+=a[right]
    return max_length