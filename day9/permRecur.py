visited = []

def perm(arr, depth, length, k):
    if (depth == k):
        print(arr)
        return
    for idx in range(depth, length):
        arr[idx], arr[depth] = arr[depth], arr[idx]
        perm(arr, depth+1, length, k)
        arr[idx], arr[depth] = arr[depth], arr[idx]


arr = [1,2,3,4,5,6]

perm(arr,0,len(arr),3)


