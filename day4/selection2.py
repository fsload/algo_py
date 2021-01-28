import random
li = []

def sort(li,i):
    while i<100:
        a = min(li[i:])
        idx = li.index(a)
        tmp = li[i]
        li[i] = li[idx]
        li[idx] = tmp
        i += 1
        return sort(li,i)

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
