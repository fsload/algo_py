graph = {
    '1' : ['2', '3'],
    '2' : ['1', '4', '5'],
    '3' : ['7'],
    '4' : ['2', '6'],
    '5' : ['2', '6'],
    '6' : ['4', '5', '7'],
    '7' : ['3', '6']
}

def dfs(graph, start_node):
    visit = list()
    stack = list()

    stack.append(start_node)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])

    return visit

print(dfs(graph,'1'))