
import unittest

import os
import sys 

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from  randomize_array import improved_fisher_yates_shuffle

class TestShuffleFunction(unittest.TestCase):

    def test_shuffle_result_length(self):
        # Test if the length of the shuffled array remains the same
        original_array = [1, 2, 3, 4, 5]
        improved_fisher_yates_shuffle(original_array)
        self.assertEqual(len(original_array), 5)

    def test_shuffle_elements(self):
        # Test if all elements from the original array are present in the shuffled array
        original_array = [1, 2, 3, 4, 5]
        improved_fisher_yates_shuffle(original_array)
        for element in original_array:
            self.assertIn(element, [1, 2, 3, 4, 5])

    def test_no_element_in_original_position(self):
        # Test if no element is in its original position after shuffling
        original_array = [1, 2, 3, 4, 5]
        improved_fisher_yates_shuffle(original_array)
        for i in range(len(original_array)):
            self.assertNotEqual(original_array[i], i + 1)

    def test_empty_array(self):
        # Test shuffling an empty array
        empty_array = []
        improved_fisher_yates_shuffle(empty_array)
        self.assertEqual(len(empty_array), 0)

if __name__ == '__main__':
    unittest.main()
