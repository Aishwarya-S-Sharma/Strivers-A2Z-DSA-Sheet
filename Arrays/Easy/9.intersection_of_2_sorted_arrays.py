a=[1,2,2,3,3,4,5]
b=[2,2,3,4,5]

#brute
visited=[0]*len(b)
res=[]
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j] and visited[j]==0:
            res.append(a[i])
            visited[j]=1
            break
        elif b[j]>a[i]:
            break

print(res)

#optimal
res=[]
i,j=0,0
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        i+=1
    elif b[j]<a[i]:
        j+=1
    else:
        res.append(a[i])
        i+=1
        j+=1
print(res)

