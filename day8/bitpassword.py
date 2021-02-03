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

print(st)
lis = []
for i in range(5):

    if '001101' in st:
        st = st.replace('001101', '')
        print(st)
        lis.append(0)
    elif '010011' in st:
        st = st.replace('010011','')
        lis.append(1)

    elif '111011' in st:
        st = st.replace('111011','')
        lis.append(2)

    elif '110001' in st:
        st = st.replace('110001','')
        lis.append(3)

    elif '100011' in st:
        st = st.replace('100011','')
        lis.append(4)

    elif '110111' in st:
        st = st.replace('110111','')
        lis.append(5)

    elif '001011' in st:
        st = st.replace('001011','')
        lis.append(6)

    elif '111101' in st:
        st = st.replace('111101','')
        lis.append(7)

    elif '011001' in st:
        st = st.replace('011001','')
        lis.append(8)

    elif '101111' in st:
        st = st.replace('101111','')
        lis.append(9)

print(lis)