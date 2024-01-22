"""
Module: string_pattern

This module provides functionality to check if a given pattern can be uniquely
mapped to a substring within a specified string.

Functions:
    string_pattern(string, pattern): Determines if a pattern can be uniquely
                                     mapped to a part of the given string.
"""

def string_pattern(string, pattern):
    """
    Check if a pattern can be uniquely mapped to a substring of the given string.

    Each unique character in the pattern must correspond to a unique character in the string.

    Parameters:
    string (str): The string in which the pattern is to be matched.
    pattern (str): The pattern that needs to be matched within the string.

    Returns:
    bool: True if the pattern can be uniquely mapped to a substring of the string, False otherwise.
    """
    for i in range(len(string) - len(pattern) + 1):
        mapping = {}
        used_chars = set()
        for j in range(len(pattern)):
            pat_char = pattern[j]
            str_char = string[i + j]

            if pat_char in mapping:
                if mapping[pat_char] != str_char:
                    break
            else:
                if str_char in used_chars:
                    break
                mapping[pat_char] = str_char
                used_chars.add(str_char)
        else:
            return True

    return False

# Examples of usage
print(string_pattern("basetestcasebase", "ABCDA")) # Expected: True
print(string_pattern("basetestcasebase", "A"))     # Expected: True
print(string_pattern("basetestcasebase", "ABA"))   # Expected: True
print(string_pattern("basetestcasebase", "AA"))    # Expected: False
print(string_pattern("abcdefg", "aa"))             # Expected: False