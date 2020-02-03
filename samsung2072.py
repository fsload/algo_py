TC = int(input())
for test_case in range(1, TC+1) :
    nums = input().split()
    nums = list(map(int,nums))
    total = [0 for i in range(TC+1)]
    for i in range(10):
        if nums[i]%2 != 0:
            total[test_case] += nums[i]
    print("#%d %d" %(test_case, total[test_case]))
