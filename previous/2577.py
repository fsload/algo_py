num = []
for i in range(3):
    num.append(int(input()))
a = num[0]
b = num[1]
c = num[2]
d = a * b * c
result = list()
for i in str(d):
    result.append(i)
result.sort()

for i in range (0, 10):
    print(result.count(str(i)))