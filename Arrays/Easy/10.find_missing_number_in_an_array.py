a=[1,2,4,5]
n=5
#brute
for i in range(1,n+1):
    flag=0
    for j in range(len(a)):
        if a[j]==i:
            flag=1
            break
    if flag==0:
        print(i)

#better
d=[0]*(n+1)
for i in range(n-1):
    d[a[i]]+=1
for i in range(1,n+1):
    if d[i]==0:
        print(i)

#optimal_1
s1=n*(n+1)//2
s2=sum(a)
print(s1-s2)

#optimal_2
xor1=0
xor2=0
for i in range(n-1):
    xor2=xor2^a[i]
    xor1=xor1^(i+1)
xor1=xor1^n
print(xor1^xor2)