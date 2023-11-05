a=[1,1,2,3,4,5]
b=[2,3,4,4,5]
#brute
#using set
s=set()
u=[]
for i in a:
    s.add(i)
for i in b:
    s.add(i)
for i in s:
    u.append(i)
print(u)

#better
#using hash map
f={}
u=[]
for i in a:
    f[i]=f.get(i,0)+1
for i in b:
    f[i]=f.get(i,0)+1
for i in f:
    u.append(i)
print(u)

#optimal
#using two pointer
i,j=0,0
u=[]
while i<len(a) and j<len(b):
    if a[i]<b[j]:
        if len(u)==0 or u[-1]!=a[i]:
            u.append(a[i])
        i+=1
    else:
        if len(u)==0 or u[-1]!=b[j]:
            u.append(b[j])
        j+=1

while i <len(a):
    if u[-1]!=a[i]:
        u.append(a[i])
    i+=1

while j<len(b):
    if u[-1]!=b[j]:
        u.append(b[j])
    j+=1

print(u)
