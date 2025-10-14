import random

def total_route_distance(route, dist_matrix):
    dist = 0
    for i in range(len(route)):
        dist += dist_matrix[route[i - 1]][route[i]]
    return dist

def get_neighbors(route):
    # Generate neighbors by swapping two cities
    neighbors = []
    for i in range(1, len(route) - 1):  # avoid depot swap at 0
        for j in range(i + 1, len(route)):
            neighbor = route[:]
            neighbor[i], neighbor[j] = neighbor[j], neighbor[i]
            neighbors.append(neighbor)
    return neighbors

def hill_climbing(dist_matrix):
    n = len(dist_matrix)
    current_route = list(range(n))  # 0 is depot
    random.shuffle(current_route[1:])  # shuffle only customers, not depot

    current_cost = total_route_distance(current_route, dist_matrix)

    while True:
        neighbors = get_neighbors(current_route)
        next_route = current_route
        next_cost = current_cost

        for neighbor in neighbors:
            cost = total_route_distance(neighbor, dist_matrix)
            if cost < next_cost:
                next_route = neighbor
                next_cost = cost

        if next_cost < current_cost:
            current_route = next_route
            current_cost = next_cost
        else:
            break  # No improvement

    return current_route, current_cost

# Example 5-node distance matrix (symmetric, 0 is depot)
dist_matrix = [
    [0, 2, 9, 10, 7],
    [2, 0, 6, 4, 3],
    [9, 6, 0, 8, 5],
    [10, 4, 8, 0, 6],
    [7, 3, 5, 6, 0]
]

route, cost = hill_climbing(dist_matrix)

print("Optimized Route:", route)
print("Total Distance: {:.2f}".format(cost))
