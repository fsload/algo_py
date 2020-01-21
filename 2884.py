n = input()

h = n.split()[0]
m = n.split()[1]

h = int(h)
m = int(m)

if h == 0 and m < 45:
    h = 23
    m = 15 + m
elif h >= 1 and m < 45:
    h = h - 1
    m = 15 + m
elif m >= 45:
    h = h
    m = m - 45

if m == 0:
    print(h)
elif m != 0:
    print(h , m)