import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from heap_sort import heap_sort


class TestHeapSort(unittest.TestCase):
    """
    Test cases for the heap_sort function.

    Each test case checks the behavior of heap_sort for different input scenarios.

    Test Cases:
    - test_empty_array: Tests heap_sort with an empty input array.
    - test_single_element: Tests heap_sort with an input array containing a single element.
    - test_increasing_order: Tests heap_sort with an input array in increasing order.
    - test_decreasing_order: Tests heap_sort with an input array in decreasing order.
    - test_random_order: Tests heap_sort with an input array in random order.
    """

    def test_empty_array(self):
        """
        Test heap_sort with an empty input array.

        Ensures that heap_sort returns an empty array for an empty input.
        """
        array = list()
        result = list()
        self.assertEqual(heap_sort(array), result)

    def test_single_element(self):
        """
        Test heap_sort with an input array containing a single element.

        Ensures that heap_sort returns the input array unchanged for a single element.
        """
        array = [1]
        result = [1]
        self.assertEqual(heap_sort(array), result)

    def test_increasing_order(self):
        """
        Test heap_sort with an input array in increasing order.

        Ensures that heap_sort correctly sorts the input array in ascending order.
        """
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(array), result)

    def test_decreasing_order(self):
        """
        Test heap_sort with an input array in decreasing order.

        Ensures that heap_sort correctly sorts the input array in ascending order.
        """
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(array), result)

    def test_random_order(self):
        """
        Test heap_sort with an input array in random order.

        Ensures that heap_sort correctly sorts the input array in ascending order.
        """
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(heap_sort(array), result)

if __name__ == "__main__":
    unittest.main()
