def comb(arr, n):
    ret = []
    if n > len(arr):
        return ret

    if n == 1:
        for i in arr:
            ret.append([i])

    elif n > 1:
        for i in range(len(arr) - n + 1):
            for temp in comb(arr[i + 1:], n - 1):
                ret.append([arr[i]] + temp)

    return ret


arr = [1,2,3,4,5,6]
n = 3

ret = comb(arr,3)

print(ret)