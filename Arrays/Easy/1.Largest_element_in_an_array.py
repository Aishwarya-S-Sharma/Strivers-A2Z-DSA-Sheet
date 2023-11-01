
#Brute Force Approach
a=[1,5,6,8,4]
a.sort()
print(a[-1])

#Optimal approach
a=list(map(int,input("Enter array elements ").split()))
largest=a[0]
for i in range(len(a)):
    if a[i]>largest:
        largest=a[i]
print(largest)
