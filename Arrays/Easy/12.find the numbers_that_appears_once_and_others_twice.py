a=[1,1,2,3,3,4,4]
#brute
for i in range(len(a)):
    e=a[i]
    c=0
    for j in range(len(a)):
        if a[j]==e:
            c+=1
    if c==1:
        print(e)

#better_1
m=max(a)
h=[0]*(m+1)
for i in a:
    h[i]+=1
for i in h:
    if h[i]==1:
        print(i)  #return i
    
#better_2
f={}
for i in a:
    if i not in f:
        f[i]=1
    else:
        f[i]+=1
for i in f:
    if f[i]==1:
        print(i)

#optimal
xor=0
for i in a:
    xor^=i
print(xor)
