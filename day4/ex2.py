ipt = input()
stack = []
li = list(ipt)
cnt = 0
for i in range (len(li)):
    if li[i] == '(':
        stack.append('(')
    elif li[i] ==')':
        if len(stack) == 0:
            cnt = 1
            break

if len(stack) != 0 or cnt == 1:
    print(False)
else:
    print(True)