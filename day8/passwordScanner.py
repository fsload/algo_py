TC = 10

#return 값으로 패스워드 여부 판단
def isPassword(sparr):
    if sparr == '0001101':
        return 0

    elif sparr == '0011001':
        return 1

    elif sparr == '0010011':
        return 2

    elif sparr == '0111101':
        return 3

    elif sparr == '0100011':
        return 4

    elif sparr == '0110001':
        return 5

    elif sparr == '0101111':
        return 6

    elif sparr == '0111011':
        return 7

    elif sparr == '0110111':
        return 8

    elif sparr == '0001011':
        return 9

    else:
        return -1  #다음 8짜리 스트링 판독


def isRight(sparr):
    if ((sparr[0] + sparr[2] + sparr[4] + sparr[6]) * 3 + sparr[1] + sparr[3] + sparr[5] + sparr[7]) % 10 == 0:
        return sparr[0] + sparr[2] + sparr[4] + sparr[6] + sparr[1] + sparr[3] + sparr[5] + sparr[7]
    elif sparr == []:
        return False
    else:
        return False

TC = int(input())

for t in range(TC):
    height,  width = map(int, input().split())
    arr = []
    for i in range(height):
        li = []
        li = input()
        li = list(li)
        arr.append(li)
    counter = 0
    sumpass = 0
    for i in range(height):
        startIdx = 0
        keepPass = []
        for j in range(width, 49, -1):
            if isPassword(''.join(arr[i][j-7:j])) != -1:
                startIdx = j
                break
        if startIdx != 0:
            for startIdx in range(j - 56, j, 7):
                toVari = []
                for k in range(startIdx, startIdx + 7):
                    toVari.append(arr[i][k])
                toVari = ''.join(toVari)
                print(toVari, isPassword(toVari))
                if isPassword(toVari) != -1:
                    keepPass.append(isPassword(toVari))
            print(keepPass)
            if isRight(keepPass) and len(keepPass) == 8:
                counter += 1
                sumpass = isRight(keepPass)
    if counter != 0:
        print('#' + str(t+1), sumpass)
    else:
        print('#' + str(t+1), 0)
