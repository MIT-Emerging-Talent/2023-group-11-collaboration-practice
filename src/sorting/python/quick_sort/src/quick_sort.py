#!  /usr/bin/env/  python 3.12
"""
Module Description: Quicksort Implementation

This module provides two implementations of the quicksort algorithm. The quicksort algorithm is a popular sorting algorithm that works by partitioning an array into smaller subarrays.

Note:
- The quicksort algorithms are recursive and efficiently sort the input lists by dividing them into smaller subarrays.
- The choice of pivot element and partitioning strategy differs between the two implementations.
- The quicksort_v2 implementation uses a 3-way partition for improved efficiency when dealing with duplicate elements.
- Random pivot selection is employed in both implementations to enhance average-case performance.

Author: Yanina Chukanova
"""
import random
from typing import List, Tuple
def quicksort_v1(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 2-way partition quicksort algorithm.
    Parameters:
    - array (List[int]): The list to be sorted.
    Returns:
    - List[int]: The sorted list.
    """
    if len(array) <= 1:
        return array
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]
    
    smaller = [x for i, x in enumerate(array) if x <= pivot and i != pivot_index]
    larger = [x for i, x in enumerate(array) if x > pivot]
    return quicksort_v1(smaller) + [pivot] + quicksort_v1(larger)
def quicksort_v2(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 3-way partition quicksort algorithm.
    Parameters:
    - array (List[int]): The list to be sorted.
    Returns:
    - List[int]: The sorted list.
    """
    if len(array) <= 1:
        return array
    pivot_index = random.randint(0, len(array) - 1)
    pivot = array[pivot_index]
    
    smaller, equal, larger = [], [], []
    for x in array:
        if x < pivot:
            smaller.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            larger.append(x)
    return quicksort_v2(smaller) + equal + quicksort_v2(larger)