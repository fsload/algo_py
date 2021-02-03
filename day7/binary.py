tr = [None] * (3 * int(13))


def getLeft(root):
    return tr[root*2 +1]

def getRight(root):
    return tr[root*2 +2]


def preorder(root):
    print(tr[root], end=' ')
    if getLeft(root):
        preorder(root*2+1)
    if getRight(root):
        preorder(root*2+2)


def inorder(root):
    if getLeft(root):
        inorder(root*2+1)

    print(tr[root], end=' ')

    if getRight(root):
        inorder(root*2+2)


def postorder(root):
    if getLeft(root):
        postorder(root*2+1)

    if getRight(root):
        postorder(root*2+2)
    print(tr[root], end=' ')


if __name__ == "__main__":
    num = input()
    li = list(input().split(' '))
    tree = []
    level = []
    for i in range(int(len(li)/2)):
        sut = []
        sut.append(li[i*2])
        sut.append(li[i*2+1])
        tree.append(sut)


    level = [0] * (3 * int(num))
    for i in range(int(len(li)/2)):
        p = li[i*2]
        s = li[i*2+1]
        if p not in tr:
            tr[0] = p
            tr[1] = s
        else:
            pidx = tr.index(p)
            if tr[pidx*2+1] != None:
                tr[pidx*2 + 2] = s
            else:
                tr[pidx*2+1] = s

    try:
        preorder(0)
    except IndexError:
        pass
    print('')
    try:
        inorder(0)
    except IndexError:
        pass
    print('')
    try:
        postorder(0)
    except IndexError:
        pass