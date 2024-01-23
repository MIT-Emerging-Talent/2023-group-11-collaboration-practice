import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from all_permutations import all_permutations

class TestAllPermutations(unittest.TestCase):
    def test_two_elements(self):
        input_list = [1, 2]
        excepted = [[1, 2], [2, 1]]
        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_three_elements(self):
        input_list = [3, 1, 2]
        excepted = [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_three_strings(self):
        input_list = ["A", "B", "C"]
        excepted = [
            ["A", "B", "C"],
            ["A", "C", "B"],
            ["B", "A", "C"],
            ["B", "C", "A"],
            ["C", "A", "B"],
            ["C", "B", "A"],
        ]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))

    def test_four_elements(self):
        input_list = [3, 1, 2, 4]
        excepted = [
            [3, 1, 2, 4],
            [3, 1, 4, 2],
            [3, 2, 1, 4],
            [3, 2, 4, 1],
            [3, 4, 1, 2],
            [3, 4, 2, 1],
            [1, 3, 2, 4],
            [1, 3, 4, 2],
            [1, 2, 3, 4],
            [1, 2, 4, 3],
            [1, 4, 3, 2],
            [1, 4, 2, 3],
            [2, 3, 1, 4],
            [2, 3, 4, 1],
            [2, 1, 3, 4],
            [2, 1, 4, 3],
            [2, 4, 3, 1],
            [2, 4, 1, 3],
            [4, 3, 1, 2],
            [4, 3, 2, 1],
            [4, 1, 3, 2],
            [4, 1, 2, 3],
            [4, 2, 3, 1],
            [4, 2, 1, 3],
        ]

        actual = all_permutations(input_list)

        self.assertListEqual(sorted(excepted), sorted(actual))


if __name__ == "__main__":
    unittest.main()
