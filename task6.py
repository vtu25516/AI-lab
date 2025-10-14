from collections import defaultdict

# Graph represented as adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B', 'G'],
    'E': ['B', 'H', 'I'],
    'F': ['C', 'J'],
    'G': ['D'],
    'H': ['E'],
    'I': ['E'],
    'J': ['F']
}

def graph_coloring(graph):
    color_map = {}
    for node in graph:
        available_colors = {1, 2, 3, 4}  # max 4 colors
        for neighbor in graph[node]:
            if neighbor in color_map and color_map[neighbor] in available_colors:
                available_colors.remove(color_map[neighbor])
        color_map[node] = min(available_colors)
    return color_map

def robot_traversal_by_color(graph, color_map):
    color_groups = defaultdict(list)
    for node, color in color_map.items():
        color_groups[color].append(node)

    print("Robot traversal by colors:")
    for color in sorted(color_groups):
        print(f"Visiting nodes with color {color}: {color_groups[color]}")

if __name__ == "__main__":
    colors = graph_coloring(graph)
    print("Node colors:", colors)
    robot_traversal_by_color(graph, colors)
