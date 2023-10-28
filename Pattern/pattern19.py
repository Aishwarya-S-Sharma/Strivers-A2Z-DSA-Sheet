'''
    A
  A B A
A B C B A
'''
n=int(input())
for i in range(n):
    print(" " * (n - i - 1), end="")
    for j in range(i + 1):
        print(chr(65 + j), end=" ")
    for j in range(i, 0, -1):
        print(chr(65 + j - 1), end=" ")
    print()
