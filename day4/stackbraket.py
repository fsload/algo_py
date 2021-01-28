TC = 10
stack = []
def braket(st):
    for i in range(len(st)):
        if st[i] == '(' or st[i] == '{' or st[i] == '[' or st[i] == '<':
            stack.append(st[i])
        elif st[i] == ')' or st[i] == '}' or st[i] == ']' or st[i] == '>':
            try:
                if st[i] == ')':
                    if stack.pop() != '(' :
                        return 0
                if st[i] == '}':
                    if stack.pop() != '{':
                        return 0
                if st[i] == ']':
                    if stack.pop() != '[':
                        return 0
                if st[i] == '>':
                    if stack.pop() != '<':
                        return 0
            except IndexError:
                return 0
    return 1

for i in range (TC):
    sddf = input()
    str1 = input()
    st = list(str1)
    print('#'+ str(i+1),braket(st))

    st.clear()