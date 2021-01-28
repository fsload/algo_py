li = []

def push(data):
    li.append(data)
def pop(arr):
    return arr.pop()
def main():
    push(1)
    push(2)
    push(3)
    print(pop(li))
    print(pop(li))
    print(pop(li))

main()