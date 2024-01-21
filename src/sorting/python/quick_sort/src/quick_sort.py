import random
from typing import List

def quicksort_v1(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 2-way partition quicksort algorithm.

    Parameters:
    - array (List[int]): The list to be sorted.

    Returns:
    - List[int]: The sorted list.
    """
    def _quicksort(array, start, stop):
        """
        Recursive function to perform 2-way partition quicksort.

        Parameters:
        - array (List[int]): The list to be sorted.
        - start (int): Start index of the sublist.
        - stop (int): Stop index of the sublist.

        Returns:
        - None
        """
        if start < stop - 1:
            pivot_index = partition(array, start, stop)
            _quicksort(array, start, pivot_index)
            _quicksort(array, pivot_index + 1, stop)

    def partition(array, start, stop):
        """
        Perform 2-way partitioning and return the index of the pivot.

        Parameters:
        - array (List[int]): The list to be partitioned.
        - start (int): Start index of the sublist.
        - stop (int): Stop index of the sublist.

        Returns:
        - int: The index of the pivot.
        """
        pivot_index = random.randint(start, stop - 1)
        array[pivot_index], array[stop - 1] = array[stop - 1], array[pivot_index]
        pivot = array[stop - 1]

        i = start
        for j in range(start, stop - 1):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

        array[i], array[stop - 1] = array[stop - 1], array[i]
        return i

    _quicksort(array, 0, len(array))
    return array


def quicksort_v2(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 3-way partition quicksort algorithm.

    Parameters:
    - array (List[int]): The list to be sorted.

    Returns:
    - List[int]: The sorted list.
    """
    def _quicksort(start: int, stop: int):
        """
        Recursive function to perform 3-way partition quicksort.

        Parameters:
        - start (int): Start index of the sublist.
        - stop (int): Stop index of the sublist.

        Returns:
        - None
        """
        if stop - start < 2:
            return
        lt, gt = partition(start, stop)
        _quicksort(start, lt)
        _quicksort(gt, stop)

    def partition(start: int, stop: int):
        """
        Perform 3-way partitioning and return the indices of the equal elements range.

        Parameters:
        - start (int): Start index of the sublist.
        - stop (int): Stop index of the sublist.

        Returns:
        - Tuple[int, int]: Indices of the equal elements range.
        """
        pivot_index = random.randint(start, stop - 1)
        pivot = array[pivot_index]

        lt, i, gt = start, start, stop
        while i < gt:
            if array[i] < pivot:
                array[i], array[lt] = array[lt], array[i]
                lt += 1
                i += 1
            elif array[i] > pivot:
                gt -= 1
                array[i], array[gt] = array[gt], array[i]
            else:
                i += 1
        return lt, gt

    _quicksort(0, len(array))
    return array