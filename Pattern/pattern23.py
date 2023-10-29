'''
*         * 
* *     * * 
* * * * * * 
* *     * * 
*         * 
'''
n=int(input())
space=2*n-2
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    for j in range(space):
        print(' ',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    space-=2
    print()
space=2
for i in range(n-1,0,-1):
    for j in range(i):
        print('*',end=' ')
    for j in range(space):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    space+=2
    print()