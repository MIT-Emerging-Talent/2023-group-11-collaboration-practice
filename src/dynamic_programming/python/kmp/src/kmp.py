def build_kmp_table(pattern):
    """
    Build the Knuth-Morris-Pratt (KMP) table for a given pattern.

    Parameters:
    - pattern (str): The pattern for which to build the KMP table.

    Returns:
    - list of int: The KMP table representing the longest prefix and suffix lengths for each position in the pattern.
    """
    m = len(pattern)
    kmp_table = [0] * m
    i, j = 1, 0

    while i < m:
        if pattern[i] == pattern[j]:
            j += 1
            kmp_table[i] = j
            i += 1
        else:
            if j != 0:
                j = kmp_table[j - 1]
            else:
                kmp_table[i] = 0
                i += 1

    return kmp_table

def find_occurrences(text, pattern):
    """
    Find all occurrences of a pattern in a given text using the Knuth-Morris-Pratt (KMP) algorithm.

    Parameters:
    - text (str): The text in which to search for occurrences of the pattern.
    - pattern (str): The pattern to search for in the text.

    Returns:
    - list of int: A list containing the starting indices of all occurrences of the pattern in the text.
    """
    n, m = len(text), len(pattern)
    if n == 0 or m == 0:
        return []

    kmp_table = build_kmp_table(pattern)
    occurrences = []
    i, j = 0, 0

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                occurrences.append(i - j)
                j = kmp_table[j - 1]
        else:
            if j != 0:
                j = kmp_table[j - 1]
            else:
                i += 1

    return occurrences

# Examples
text1 = "abcdefghijklmnopqrstuvwxyz"
pattern1 = "bc"
print(find_occurrences(text1, pattern1))  # Output: [1]

text2 = "abcabcabcabc"
pattern2 = "abc"
print(find_occurrences(text2, pattern2))  # Output: [0, 3, 6, 9]
