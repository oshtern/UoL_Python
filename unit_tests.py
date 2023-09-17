# Importing only the necessary functions within the module
import unittest

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
    return min(calculate_shortest_path(i, j, k - 1, v),
               calculate_shortest_path(i, k, k - 1, v) + calculate_shortest_path(k, j, k - 1, v))


def solve_paths(graph):
    # Replacing all values within the graph with the shortest paths
    for start, end, interim in product(range(len(graph)), repeat=3):
        # Calls the "shortest_path" function for each combination of "start" and "end"
        graph[start][end] = calculate_shortest_path(start, end, interim, graph)
    return graph


class Test(unittest.TestCase):
    def test_one(self):
        test = [[0, 5, no_path, 10],
                [no_path, 0, 3, no_path],
                [no_path, no_path, 0, 1],
                [no_path, no_path, no_path, 0]]

        expected = [[0, 5, 8, 9],
                    [no_path, 0, 3, 4],
                    [no_path, no_path, 0, 1],
                    [no_path, no_path, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)

    def test_two(self):
        test = [[0, 6, 2, no_path],
                [no_path, 0, no_path, 2],
                [no_path, no_path, 0, 6],
                [no_path, no_path, no_path, 0]]

        expected = [[0, 6, 2, 8],
                    [no_path, 0, no_path, 2],
                    [no_path, no_path, 0, 6],
                    [no_path, no_path, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)

    def test_three(self):
        test = [[0, 6, 2, 8],
                [2, 0, no_path, no_path],
                [5, 3, 0, 8],
                [no_path, 2, no_path, 0]]

        expected = [[0, 5, 2, 8],
                    [2, 0, no_path, no_path],
                    [5, 3, 0, 8],
                    [4, 2, no_path, 0]]

        result = solve_paths(test)
        self.assertEqual(solve_paths(test), expected)


if __name__ == '__main__':
    unittest.main()
