# String Search with Knuth-Morris-Pratt Algorithm

This project implements the Knuth-Morris-Pratt (KMP) algorithm for efficient string searching in Python.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Testing](#testing)

## Overview

The Knuth-Morris-Pratt (KMP) algorithm is a string-searching algorithm that efficiently finds all occurrences of a pattern in a given text. The algorithm preprocesses the pattern to create a table, which is then used to skip unnecessary comparisons during the search, reducing the overall time complexity.

This project provides a Python implementation of the KMP algorithm, including functions for building the KMP table (`build_kmp_table`) and finding occurrences in a text (`find_occurrences`).

## Installation

Clone the repository to your local machine:

```bash
git clone ...


```

## Usage

To use the KMP algorithm in your Python project, import the relevant functions from the module:

```python
from kmp import build_kmp_table, find_occurrences
```

You can then call these functions with your text and pattern to find occurrences:

```python
text = "ababcabcab"
pattern = "abc"

kmp_table = build_kmp_table(pattern)
occurrences = find_occurrences(text, pattern)

print(f"Occurrences of '{pattern}' in '{text}': {occurrences}")
```

## Examples

# Example 1

text1 = "abcdefghijklmnopqrstuvwxyz"
pattern1 = "bc"
print(find_occurrences(text1, pattern1)) # Output: [1]

# Example 2

text2 = "abcabcabcabc"
pattern2 = "abc"
print(find_occurrences(text2, pattern2)) # Output: [0, 3, 6, 9]

## Testing

The project includes test cases to ensure the correctness of the implemented functions. To run the tests, execute the test script:

```bash
./run_tests.sh --python --exercise=kmp
```
