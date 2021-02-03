n = int(input())

cnt = 0
int(cnt)
if n == 1 or n == 2 or n == 7 or n == 4:
    cnt = -1
elif n%5 == 0:
    cnt = n//5
elif n%5 == 1:
    cnt = n//5 + 1
elif n%5 == 2:
    cnt = n//5 + 2
elif n%5 == 3:
    cnt = n//5 + 1
elif n%5 == 4:
    cnt = n//5 + 2

print(cnt)