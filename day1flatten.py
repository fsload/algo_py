ma = 0
mi = 100
for i in range(10):
    num = int(input())
    li = list(map(int,input().split()))
    for i in range(num):
        for j in range(100):
            ma = max(li)
            mi = min(li)
            if ma in li:
                idx = li.index(ma)
                li[idx] -= 1
            if mi in li:
                idx = li.index(ma)
                li[idx] += 1
    print('#',i+1, ' ', ma-mi)