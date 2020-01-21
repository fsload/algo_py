a = int(input())
b = input().split()
b = list(map(int, b))

print(min(b), max(b))

#map(int, input().split())으로 받고 sort하는 경우 에러가 뜸
#5