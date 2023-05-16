def dfs(node, graph, visited, component):
    component.append(node)
    visited[node] = True

    for child in graph[node]:
        if not visited[child]:
            dfs(child, graph, visited, component)


if __name__ == "__main__":

    graph = {
        0: [2],
        1: [2, 3],
        2: [0, 1, 4],
        3: [1, 4],
        4: [2, 3]
    }
    node = 0
    visited = [False]*len(graph)
    component = []
    dfs(node, graph, visited, component)
    print(f"Following is the Depth-first search: {component}")

# TS: #TS : O(B^d)
