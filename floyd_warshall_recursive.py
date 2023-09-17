# Only importing the necessary functions vithin a module
from sys import maxsize
from itertools import product

no_path = maxsize


def calculate_shortest_path(i, j, k, v):
    # Calculating the shortest path between "i" and "j"
    if k == 0:
        if i == j:
            return 0
        return v[i][j]
    # Recursive call to the function
    return min(calculate_shortest_path(i, j, k - 1, v), calculate_shortest_path(i, k, k - 1, v) + calculate_shortest_path(k, j, k - 1, v))


def solve_paths(graph):
    # Replacing all values within the graph with the shortest paths
    for start, end, interim in product(range(len(graph)), repeat=3):
        # Calls the "shortest_path" function for each combination of "start" and "end"
        graph[start][end] = calculate_shortest_path(start, end, interim, graph)
    return graph
