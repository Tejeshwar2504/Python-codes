def splitArr(a, n, k):
    b = a[:k]
    return (a[k::]+b[::])
arr = [17,32,8,63,6]
n = len(arr)
position = 2
arr = splitArr(arr, n, position)
for i in range(0, n):
    print(arr[i], end=' ')