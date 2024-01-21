import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from insertion_sort import insertionsort_v2

class TestInsertionSortV2(unittest.TestCase):
    """
    Test cases for the insertionsort_v2 function.
    """

    def test_empty_array(self):
        """
        Test sorting an empty array.
        """
        array = []
        result = []
        self.assertEqual(insertionsort_v2(array), result)

    def test_single_element(self):
        """
        Test sorting an array with a single element.
        """
        array = [1]
        result = [1]
        self.assertEqual(insertionsort_v2(array), result)

    def test_increasing_order(self):
        """
        Test sorting an array in increasing order.
        """
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(insertionsort_v2(array), result)

    def test_decreasing_order(self):
        """
        Test sorting an array in decreasing order.
        """
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(insertionsort_v2(array), result)

    def test_random_order(self):
        """
        Test sorting an array in random order.
        """
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(insertionsort_v2(array), result)

    def test_string_elements(self):
        """
        Test sorting an array with string elements.
        """
        array = ['banana', 'apple', 'orange', 'grape']
        result = ['apple', 'banana', 'grape', 'orange']
        self.assertEqual(insertionsort_v2(array), result)


if __name__ == "__main__":
    unittest.main()
