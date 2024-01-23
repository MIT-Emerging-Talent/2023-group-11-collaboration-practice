import unittest

import os
import sys

file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from is_palindrome_after_char_deletion import is_palindrome_after_char_deletion


class TestIsPalindromeAfterCharDeletion(unittest.TestCase):
    """
    Test cases for the is_palindrome_after_char_deletion function.

    Each test case checks the behavior of is_palindrome_after_char_deletion for different input strings.

    Test Cases:
    - test_1: Tests is_palindrome_after_char_deletion with a palindrome input string.
    - test_2: Tests is_palindrome_after_char_deletion with a non-palindrome input string.
    - test_3: Tests is_palindrome_after_char_deletion with a palindrome input string.
    - test_4: Tests is_palindrome_after_char_deletion with a palindrome input string.
    - test_5: Tests is_palindrome_after_char_deletion with a palindrome input string.
    - test_6: Tests is_palindrome_after_char_deletion with a palindrome input string.
    - test_7: Tests is_palindrome_after_char_deletion with a non-palindrome input string.
    """

    def test_1(self):
        """
        Test is_palindrome_after_char_deletion with a palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns True for a palindrome input.
        """
        input_string = "racecar"
        expected = True
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_2(self):
        """
        Test is_palindrome_after_char_deletion with a non-palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns False for a non-palindrome input.
        """
        input_string = "hello"
        expected = False
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_3(self):
        """
        Test is_palindrome_after_char_deletion with a palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns True for a palindrome input.
        """
        input_string = "abcba"
        expected = True
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_4(self):
        """
        Test is_palindrome_after_char_deletion with a palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns True for a palindrome input.
        """
        input_string = "abcdefghhgfedcba"
        expected = True
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_5(self):
        """
        Test is_palindrome_after_char_deletion with a palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns True for a palindrome input.
        """
        input_string = "abcdefgfedcba"
        expected = True
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_6(self):
        """
        Test is_palindrome_after_char_deletion with a palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns True for a palindrome input.
        """
        input_string = "abcdefghijklmnonmlkjihgfedcba"
        expected = True
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)

    def test_7(self):
        """
        Test is_palindrome_after_char_deletion with a non-palindrome input string.

        Ensures that is_palindrome_after_char_deletion returns False for a non-palindrome input.
        """
        input_string = "abcdefghijklmnopqrstuvwxyzdcba"
        expected = False
        actual = is_palindrome_after_char_deletion(input_string)
        self.assertEqual(actual, expected)


if __name__ == "__main__":
    unittest.main()
