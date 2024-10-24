def dfs(graph, start, curr_path, all_paths, visited):
    # Add the current node to the path
    curr_path.append(start)

    # Mark the current node as visited
    visited.add(start)

    # If the current node has no neighbors or all neighbors are visited, it's a leaf node, so save the path
    if not graph[start] or all(child in visited for child in graph[start]):
        all_paths.append(curr_path.copy())
    else:
        # Recur for all unvisited neighbors of the current node
        for child in graph[start]:
            if child not in visited:
                dfs(graph, child, curr_path, all_paths, visited)

    # Backtrack: remove the current node from the path
    curr_path.pop()


def review_sort_path(graph):
    all_paths = []
    visited = set()

    # Start DFS from each node to explore all paths
    for start_node in graph:
        if start_node not in visited:
            curr_path = []
            dfs(graph, start_node, curr_path, all_paths, visited)

    return all_paths



