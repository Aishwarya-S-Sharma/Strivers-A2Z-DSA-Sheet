a=[1,1,0,1,1,1,0,1,1]
c=0
m=0
for i in range(len(a)):
    if a[i]==1:
        c+=1
    else:
        c=0
    m=max(m,c)
print(m)