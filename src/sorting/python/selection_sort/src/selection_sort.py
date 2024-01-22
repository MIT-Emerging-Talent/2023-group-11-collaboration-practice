#!/usr/bin/env python3.12

"""
Module Description: 

This Python module implements the Selection Sort algorithm. 
Selection Sort is a simple comparison-based sorting algorithm that divides the input list into a sorted and an unsorted region. 
It repeatedly selects the minimum element from the unsorted region and swaps it with the first element in the unsorted region.


Author:
Dmytro Lytvynenko
"""


def selection_sort(arr):
    for i in range(len(arr)):
        """
        Find minimum element
        """
        mini = min(arr[i:])
        """
        Find index of minimum element
        """
        min_index = arr[i:].index(mini)
        """
        Replace element at min_index with first element
        """
        arr[i + min_index] = arr[i]
        """
        Replace first element with min element
        """
        arr[i] = mini
    """
    Return sorted list
    """
    return arr
