# Insertion Sort

This project implements the insertion sort algorithm in Python.

## Description

Insertion sort is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort.

## Usage

The `insertionsort_v2` function is provided in the `insertion_sort` module to perform insertion sort on an input array.

### Example

```python
from insertion_sort import insertionsort_v2

array = [4, 2, 7, 1, 9, 5]
sorted_array = insertionsort_v2(array)

print("Original Array:", array)
print("Sorted Array:", sorted_array)
```
