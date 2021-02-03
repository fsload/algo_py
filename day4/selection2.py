import random
li = []

def sort(li,i):
    while i<100:
        print(i)
        a = min(li[i:])
        idx = li.index(a)
        tmp = li[i]
        li[i] = li[idx]
        li[idx] = tmp
        i += 1
        sort(li,i)

while True:
    i = random.randint(1, 100)
    if i not in li:
        li.append(i)
        if len(li) == 100:
            break

print('before sort : ', li)
i = 0

sort(li,i)
print('after sort : ', li)




func(list , curIdx)


func([4,2,1,5,3], 0)
|
func([1,2,4,5,3], 1)
|
func()
|
func([1,2,3,4,5]. 4) ==> if curIdx == len - 1


func([0 .. 1], 0)  --- func([0 .. 1] 1) ------------------ func()
                                         ----------------- func(78)
                   --- func([], 2)