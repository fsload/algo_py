TC = 10
st = 0
def mul(multi,num,power,st):
    multi *= num
    if st != power -1:
        return mul(multi,num,power,st+1)
    else:
        return multi

for t in range (TC):
    multi = 1
    i = input()
    num, power = input().split()
    num = int(num)
    power = int(power)
    print('#'+ str(t+1), mul(num,num,power,1))