'''
E
DE
CDE
BCDE
ABCDE
'''
n=int(input())
for i in range(n):
    for j in range(i+1):
        print(chr(65+n-1-j),end=" ")
    print()