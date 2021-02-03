count = 0
a = input()
length = len(a)
n = int(a)
for i in range(100, n):
    for j in range (0, length-2):
        if int(a[j]) - int(a[j+1]) == int(a[j+1]) - int(a[j+2]):
            count = count + 1
if length >= 3:
    count + 99
else:
    count = n
print(count)
print(length)
