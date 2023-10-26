#printing a square
#approach 1
n=int(input())
for i in range(n):
    print('* '*n)

#approach 2
n=int(input())
for i in range(n):
    for j in range(n):
        print('*',end=' ')
    print()

