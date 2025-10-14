import numpy as np

class AntColony:
    def __init__(self, cities, dist_matrix, n_ants, n_best, n_iterations, decay, alpha=1, beta=2):
        """
        cities: list of city names
        dist_matrix: 2D numpy array of distances between cities
        """
        self.cities = cities
        self.dist_matrix = dist_matrix
        self.pheromone = np.ones(self.dist_matrix.shape) / len(dist_matrix)
        self.all_inds = range(len(dist_matrix))
        self.n_ants = n_ants
        self.n_best = n_best
        self.n_iterations = n_iterations
        self.decay = decay
        self.alpha = alpha
        self.beta = beta

    def run(self):
        shortest_path = None
        all_time_shortest_path = ("placeholder", np.inf)
        for i in range(self.n_iterations):
            all_paths = self.gen_all_paths()
            self.spread_pheromone(all_paths, self.n_best)
            shortest_path = min(all_paths, key=lambda x: x[1])
            if shortest_path[1] < all_time_shortest_path[1]:
                all_time_shortest_path = shortest_path            
            self.pheromone *= self.decay
        return all_time_shortest_path

    def gen_path_dist(self, path):
        total_dist = 0
        for i in range(len(path) - 1):
            total_dist += self.dist_matrix[path[i]][path[i + 1]]
        return total_dist

    def gen_all_paths(self):
        all_paths = []
        for _ in range(self.n_ants):
            path = self.gen_path(0)  # start from city 0 (depot)
            dist = self.gen_path_dist(path)
            all_paths.append((path, dist))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        path.append(start)
        prev = start
        for _ in range(len(self.dist_matrix) - 1):
            move = self.pick_move(self.pheromone[prev], self.dist_matrix[prev], visited)
            path.append(move)
            visited.add(move)
            prev = move
        path.append(start)  # return to start city
        return path

    def pick_move(self, pheromone, distances, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0  # don't revisit cities

        row = pheromone ** self.alpha * ((1.0 / distances) ** self.beta)
        norm_row = row / row.sum()
        move = np.random.choice(self.all_inds, 1, p=norm_row)[0]
        return move

    def spread_pheromone(self, all_paths, n_best):
        sorted_paths = sorted(all_paths, key=lambda x: x[1])
        for path, dist in sorted_paths[:n_best]:
            for move in range(len(path) - 1):
                self.pheromone[path[move]][path[move + 1]] += 1.0 / self.dist_matrix[path[move]][path[move + 1]]

def path_to_cities(path, cities):
    return [cities[i] for i in path]

if __name__ == "__main__":
    cities = ['A', 'B', 'C', 'D', 'E']
    dist_matrix = np.array([
        [np.inf, 2, 2, 5, 7],
        [2, np.inf, 4, 8, 2],
        [2, 4, np.inf, 1, 3],
        [5, 8, 1, np.inf, 2],
        [7, 2, 3, 2, np.inf]
    ])

    ant_colony = AntColony(cities, dist_matrix, n_ants=10, n_best=3, n_iterations=100, decay=0.95, alpha=1, beta=2)
    best_path_indices, best_dist = ant_colony.run()
    best_path_cities = path_to_cities(best_path_indices, cities)

    print("Best path:", " -> ".join(best_path_cities))
    print("Total distance:", best_dist)
