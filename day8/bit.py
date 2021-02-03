li = list(input())

bit = []
bi = []
for i in range(len(li)):
    bi.append(li[i])
    if i % 7 == 6:
        bit.append(bi)
        bi = []

for i in range(len(bit)):
    sum = 0
    for j in range(len(bit[i]) -1 , -1, -1):
        if bit[i][j] == '1':
            # print(len(bit)-j - 4)
            sum += 1 * (2 ** (len(bit[i]) - j - 1))
    print(sum)
