'''
1                 1
1 2             2 1
1 2 3         3 2 1
1 2 3 4     4 3 2 1
1 2 3 4 5 5 4 3 2 1
'''
n=int(input())
space=2*(n-1)
for i in range(1,n+1):
    #numbers
    for j in range(1,i+1):
        print(j,end=' ')
    #space
    for j in range(1,space+1):
        print(' ',end=' ')
    #numbers
    for j in range(i,0,-1):
        print(j,end=' ')
    print()
    space-=2
