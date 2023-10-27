'''
    *    
   ***   
  *****  
 ******* 
*********
*********
 ******* 
  *****  
   ***   
    *   
'''

n=int(input())
for i in range(n):
    for j in range(n-i-1): #space 
        print(' ',end='')
    for j in range(2*i+1): #star
        print('*',end='')
    for j in range(n-i-1): #space
        print(' ',end='')
    print()
for i in range(n):
    for j in range(i): #space 
        print(' ',end='')
    for j in range(2*n-(2*i+1)): #star
        print('*',end='')
    for j in range(i): #space
        print(' ',end='')
    print()