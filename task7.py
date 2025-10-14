from collections import deque

# Graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],  # Tool is here
    'I': ['E'],
    'J': ['F']
}

robot_location = 'A'  # Robot starting location
tool_location = 'H'   # Tool location

def bfs_path(graph, start, target):
    queue = deque([(start, [start])])  # (current_node, path_taken)
    visited = set()

    while queue:
        current_node, path = queue.popleft()

        if current_node == target:
            return path

        visited.add(current_node)

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return None

if __name__ == "__main__":
    path_to_tool = bfs_path(graph, robot_location, tool_location)

    if path_to_tool:
        print(f"Robot path to fetch the tool: {' -> '.join(path_to_tool)}")
    else:
        print("Tool not found in the graph.")
