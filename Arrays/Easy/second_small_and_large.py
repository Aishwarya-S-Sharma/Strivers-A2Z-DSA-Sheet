#Brute
a=[2,1,5,6,8,7]
a.sort()
print(a[1],a[-2])

#Better
def getElements(arr, n):
    if n == 0 or n == 1:
        print(-1, -1)  # edge case when only one element is present in array
    small = float('inf')
    second_small = float('inf')
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        small = min(small, arr[i])
        large = max(large, arr[i])
    for i in range(n):
        if arr[i] < second_small and arr[i] != small:
            second_small = arr[i]
        if arr[i] > second_large and arr[i] != large:
            second_large = arr[i]
    print("Second smallest is", second_small)
    print("Second largest is", second_large)


#optimal
def second_small(arr,n):
    if n<2:
        return -1
    small=float('inf')
    second_small=float('inf')
    for i in range(n):
        if arr[i]<small:
            second_small=small
            small=arr[i]
        elif arr[i]<second_small and arr[i]!=small:
            second_small=arr[i]
    return second_small

def second_large(arr,n):
    if n<2:
        return -1
    large=float('-inf')
    second_large=float('-inf')
    for i in range(n):
        if arr[i]>large:
            second_large=large
            large=arr[i]
        elif arr[i]<second_large and arr[i]!=large:
            second_large=arr[i]
    return second_large