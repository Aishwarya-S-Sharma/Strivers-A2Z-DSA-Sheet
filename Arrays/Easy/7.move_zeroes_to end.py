a=[1,0,2,3,2,0,0,4,5,1]
n=len(a)

#brute
temp=[]
for i in range(n):
    if a[i]!=0:
        temp.append(a[i])
x=len(temp)
for i in range(x):
    a[i]=temp[i]

for i in range(x,n):
    a[i]=0

print(a)


#optimal
j=-1
for i in range(n):
    if a[i]==0:
        j=i
        break

if j==-1:   #if no zeroes in array
    print(a)  #return a

for i in range(j+1,n):
    if a[i]!=0:
        a[i],a[j]=a[j],a[i]
        j+=1
print(a)