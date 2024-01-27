def max_el_row(mat,n,m,col):
    max_val=float('-inf')
    max_ind=-1
    for i in range(n):
        if mat[i][col]>max_val:
            max_val=mat[i][col]
            max_ind=i
    return max_ind
def findPeakGrid(g):
    n=len(g)
    m=len(g[0])
    low,high=0,m-1
    while low<=high:
        mid=(low+high)//2
        row=max_el_row(g,n,m,mid)
        left= g[row][mid-1] if mid-1>=0 else -1
        right=g[row][mid+1] if mid+1<m  else -1
        if g[row][mid]>left and g[row][mid]>right:
            return row,mid
        elif g[row][mid]<left:
            high=mid-1
        else:
            low=mid+1
    return -1,-1

mat = [[10,20,15],[21,30,14],[7,16,32]]
print("The peak element is at ",findPeakGrid(mat))