# Selection Sort Algorithm

## Overview

This Python module implements the Selection Sort algorithm. Selection Sort is a simple comparison-based sorting algorithm that divides the input list into a sorted and an unsorted region. It repeatedly selects the minimum element from the unsorted region and swaps it with the first element in the unsorted region.

## Author

- **Dmytro Lytvynenko**

## Module Description

This module provides a single function `selectionsort_v1` for sorting a given list using the Selection Sort algorithm.

### Behavior Description

The `selectionsort_v1` function sorts a list of comparable elements using the Selection Sort algorithm. It modifies the input list in-place and returns the sorted list.

### Parameter Description

- **arr (list):** The list of comparable elements to be sorted.

### Return Value Description

- **list:** The sorted list containing the same elements as the input list.

## Usage

To use the `selectionsort_v1` function, import it into your Python script or module and call it with a list of comparable elements.

```python
from selection_sort import selection_sort

# Example usage
my_list = [4, 2, 7, 1, 9]
sorted_list = selection_sort(my_list)
print(sorted_list)


