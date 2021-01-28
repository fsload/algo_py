import random
li = []

def sort(li):
    for i in range (100):
        for j in range(i, 100):
            a = min(li[i:])
            idx = li.index(a)
            tmp = li[i]
            li[i] = li[idx]
            li[idx] = tmp

    return li

while True:
    i = random.randint(1, 100)
    if i not in li:
        li.append(i)
        if len(li) == 100:
            break

print('before sort : ', li)
print('after sort : ', sort(li))