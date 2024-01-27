#Brute
def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(n):
        cnt_ones = sum(matrix[i])
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

#Optimal
def lower_bound(nums,n,target):
    low=0
    high=n-1
    ans=n
    while low<=high:
        mid=(low+high)//2            
        if nums[mid]>=target:
            ans=mid
            high=mid-1
        else:
            low=mid+1
    return ans

def rowWithMax1s(matrix, n, m):
    cnt_max = 0
    index = -1

    # traverse the matrix:
    for i in range(n):
        cnt_ones = m-lower_bound(matrix[i],m,1)
        if cnt_ones > cnt_max:
            cnt_max = cnt_ones
            index = i
    return index

matrix = [[1, 1, 1], [0, 0, 1], [0, 0, 0]]
n = 3
m = 3
print("The row with maximum no. of 1's is:", rowWithMax1s(matrix, n, m))
