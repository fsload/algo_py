num = input().split()
a = num[0]
b = num[1]
a = a[::-1]
b = b[::-1]


if int(a) > int(b):
    print(a)
else:
    print(b)