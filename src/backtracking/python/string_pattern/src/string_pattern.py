def string_pattern(string, pattern):
    """
    Check if the pattern matches anywhere in the string.
    Each unique character in the pattern represents a unique character in the string,
    and the same characters in the pattern represent the same characters in the string.
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

