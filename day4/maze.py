s = input()
maze =[]
visited = []
stack = []
for i in range(16):
    maze.append(list(input()))


def dfs(X, Y):
    if maze(X, Y) == 0:
        visited.append([X,Y])
        for path in maze:


    while stack:
        ret = stack.pop()
        if ret == 3:
            return 1
        else:
            if graph[start + 1, j] == 0:



print(maze)