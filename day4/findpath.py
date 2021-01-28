graph = {}
TC = 10


def dfs(graph,start):
    visited = list()
    stack = list()

    stack.append(start)

    while stack:
        node = stack.pop()

        if node == 99:
            return 1

        elif node not in visited:
            visited.append(node)
            if node in graph:
                for vis in graph[node]:
                    stack.append(vis)

    return 0


for t in range(TC):
    a, b = map(int, input().split())
    it = list(map(int, input().split()))
    for i in range(0, len(it), 2):
        if it[i] in graph:
            graph[it[i]].append(it[i + 1])
        else:
            graph[it[i]] = [it[i + 1]]

    print('#'+ str(t+1), dfs(graph,0))
    graph.clear()