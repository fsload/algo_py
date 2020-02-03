for test_case in range (1, 11):
    n = int(input())
    bilding = input().split()
    bilding = list(map(int, bilding))
    total = [0 for i in range(11)]
    for i in range (2, n-2):
        if bilding[i] > max(bilding[i-2], bilding[i-1] , bilding[i+1], bilding[i+2]):
            total[test_case] +=  bilding[i] - max(bilding[i-2], bilding[i-1] , bilding[i+1], bilding[i+2]) 

    print("#%d %d" %(test_case, total[test_case]))