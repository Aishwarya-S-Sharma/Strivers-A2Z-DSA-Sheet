#Brute
def searchMatrix(mat: [[int]], target: int) -> bool:
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j]==target:
                return True
    return False


#Better
def search(nums: [int], target: int):
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

def searchMatrix(mat: [[int]], target: int) -> bool:
    n=len(mat)
    m=len(mat[0])
    for i in range(n):
        if mat[i][0]<=target and target<=mat[i][m-1]:
            return search(mat[i],target)
    return False
        
#Optimal

def searchMatrix(mat: [[int]], target: int) -> bool:
    n=len(mat)
    m=len(mat[0])
    low,high=0,n*m-1
    while low<=high:
        mid=(low+high)//2
        row,col=mid//m,mid%m
        if mat[row][col]==target:
            return True
        elif mat[row][col]<target:
            low=mid+1
        else:
            high=mid-1
    return False
        
matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result = searchMatrix(matrix, 8)
print("true" if result else "false")