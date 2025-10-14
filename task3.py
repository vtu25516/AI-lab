import heapq

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    rows, cols = len(grid), len(grid[0])
    open_set = []
    heapq.heappush(open_set, (0 + heuristic(start, goal), 0, start, [start]))

    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)

        if current == goal:
            return path

        if current in visited:
            continue
        visited.add(current)

        x, y = current
        neighbors = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]

        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 0 and (nx, ny) not in visited:
                    new_g = g + 1
                    new_f = new_g + heuristic((nx, ny), goal)
                    heapq.heappush(open_set, (new_f, new_g, (nx, ny), path + [(nx, ny)]))

    return None  # No path found

# Example grid: 0 = walkable, 1 = obstacle
grid_map = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0],
]

start = (0, 0)
goal = (4, 4)

path = a_star(grid_map, start, goal)

if path:
    print("Path found:")
    for step in path:
        print(step)
else:
    print("No path found.")
