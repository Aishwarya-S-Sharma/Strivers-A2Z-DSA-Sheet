#Brute
def searchElement(matrix, target):
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        for j in range(m):
            if matrix[i][j]==target:
                return True
    return False

#Better
def search(nums, target):
    n=len(nums)
    low=0
    high=n-1
    while low<=high:
        mid=(low+high)//2
        if nums[mid]==target:
            return True
        elif nums[mid]>target:
            high=mid-1
        else:
            low=mid+1
    return False
def searchElement(matrix, target) -> int:
    n=len(matrix)
    m=len(matrix[0])
    for i in range(n):
        ind=search(matrix[i],target)
        if ind!=-1:
            return True
    return False
    
#Optimal
def searchElement(matrix, target):
    n=len(matrix)
    m=len(matrix[0])
    row,col=0,m-1
    while row<n and col>=0:
        if matrix[row][col]==target:
            return True
        elif matrix[row][col]<target:
            row+=1
        else:
            col-=1
    return False

matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchElement(matrix, 8)
print("true" if result else "false")