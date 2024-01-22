import unittest
import os
import sys

file = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file + "/src")


from kmp import build_kmp_table, find_occurrences

class TestStringSearchFunctions(unittest.TestCase):

    def test_build_kmp_table(self):
        # Test Case 1: Valid pattern with no repeated characters
        pattern1 = "abcde"
        self.assertEqual(build_kmp_table(pattern1), [0, 0, 0, 0, 0])

        # Test Case 2: Valid pattern with repeated characters
        pattern2 = "aabcaabx"
        self.assertEqual(build_kmp_table(pattern2), [0, 1, 0, 0, 1, 2, 3, 0])

        # Test Case 3: Empty pattern
        pattern3 = ""
        self.assertEqual(build_kmp_table(pattern3), [])

    def test_find_occurrences(self):
        # Test Case 1: Valid occurrences in the middle of the text
        text1 = "ababcabcab"
        pattern1 = "abc"
        self.assertEqual(find_occurrences(text1, pattern1), [2, 5])

        # Test Case 2: Valid occurrences at the beginning and end of the text
        text2 = "abcabcabcdabc"
        pattern2 = "abc"
        self.assertEqual(find_occurrences(text2, pattern2), [0, 3, 6, 10])

        # Test Case 3: No occurrences in the text
        text3 = "xyz"
        pattern3 = "abc"
        self.assertEqual(find_occurrences(text3, pattern3), [])

        # Test Case 4: Empty pattern
        text4 = "abc"
        pattern4 = ""
        self.assertEqual(find_occurrences(text4, pattern4), [])

if __name__ == '__main__':
    unittest.main()
