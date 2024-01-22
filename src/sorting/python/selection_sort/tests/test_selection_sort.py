import os
import sys
import unittest

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from selection_sort import selection_sort


class TestSelectionSortV1(unittest.TestCase):
    """
    Test cases for the selectionsort_v1 function.
    """

    def test_empty_array(self):
        """
        Test sorting an empty array.

        Args: None

        Returns: None

        Asserts: The result should also be an empty array.
        """
        array = list()
        result = list()
        self.assertEqual(selection_sort(array), result)

    def test_single_element(self):
        """
        Test sorting an array with a single element.

        Args: None

        Returns: None

        Asserts: The result should be the same single element.
        """
        array = [1]
        result = [1]
        self.assertEqual(selection_sort(array), result)

    def test_increasing_order(self):
        """
        Test sorting an array in increasing order.

        Args: None

        Returns: None

        Asserts: The result should be the same array.
        """
        array = [1, 2, 3, 4, 5]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(array), result)

    def test_decreasing_order(self):
        """
        Test sorting an array in decreasing order.

        Args: None

        Returns: None

        Asserts: The result should be the array in increasing order.
        """
        array = [5, 4, 3, 2, 1]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(array), result)

    def test_random_order(self):
        """
        Test sorting an array in random order.

        Args: None

        Returns: None

        Asserts: The result should be the array in increasing order.
        """
        array = [2, 5, 1, 4, 3]
        result = [1, 2, 3, 4, 5]
        self.assertEqual(selection_sort(array), result)


if __name__ == "__main__":
    unittest.main()
