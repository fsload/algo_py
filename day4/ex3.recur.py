graph = {
    '1' : ['2', '3'],
    '2' : ['1', '4', '5'],
    '3' : ['7'],
    '4' : ['2', '6'],
    '5' : ['2', '6'],
    '6' : ['4', '5', '7'],
    '7' : ['3', '6']
}

visited = []

def dfs(graph, start):
    visited.append(start)

    for node in graph[start]:
        if node not in visited:
            dfs(graph,node)

    return visited

print(dfs(graph,'1'))