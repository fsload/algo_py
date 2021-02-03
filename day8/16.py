li = list(input())
st = []

for i in range(len(li)):
    if li[i] == '0':
        st.append('0000')
    elif li[i] == '1':
        st.append('0001')
    elif li[i] == '2':
        st.append('0010')
    elif li[i] == '3':
        st.append('0011')
    elif li[i] == '4':
        st.append('0100')
    elif li[i] == '5':
        st.append('0101')
    elif li[i] == '6':
        st.append('0110')
    elif li[i] == '7':
        st.append('0111')
    elif li[i] == '8':
        st.append('1000')
    elif li[i] == '9':
        st.append('1001')
    elif li[i] == 'A':
        st.append('1010')
    elif li[i] == 'B':
        st.append('1011')
    elif li[i] == 'C':
        st.append('1100')
    elif li[i] == 'D':
        st.append('1101')
    elif li[i] == 'E':
        st.append('1110')
    elif li[i] == 'F':
        st.append('1111')

st = ''.join(st)
bit = []
bi = []
li = list(st)
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