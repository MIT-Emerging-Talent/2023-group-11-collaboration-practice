# quicksort.py: 
Python script containing the implementations of in-place 2-way partition QuickSort (quicksort_v1) 
and in-place 3-way partition QuickSort (quicksort_v2).
# Usage
In-Place 2-Way Partition QuickSort
To use the in-place 2-way partition QuickSort, import the quicksort_v1 function and provide a list of integers to be sorted.

# quicksort_v1
# Function Signature
python
def quicksort_v1(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 2-way partition QuickSort algorithm.

    Parameters:
    - array (List[int]): The list to be sorted.

    Returns:
    - List[int]: The sorted list.
    """
    ...
# Documentation
The quicksort_v1 function implements the QuickSort algorithm using in-place 2-way partitioning. It takes a list of integers as input and sorts the list in ascending order. The function modifies the input list in-place and returns the sorted list.

# Behavior
The quicksort_v1 function sorts the input list in-place using the 2-way partition QuickSort algorithm. It follows the divide-and-conquer approach, selecting a pivot element and rearranging the elements in the list such that elements less than the pivot are on the left, and elements greater than the pivot are on the right. The process is applied recursively to sublists until the entire list is sorted.

# Attributes
array (List[int]): The list of integers to be sorted in-place.

# Returns
List[int]: The sorted list.

# Explanation
The function modifies the input list (array) in-place, sorting it in ascending order.
It uses the 2-way partitioning scheme, randomly selecting a pivot and rearranging elements accordingly.
The return value is the same list object after sorting.

# Example
from quicksort import quicksort_v1
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quicksort_v1(array)
print("Sorted Array:", sorted_array)


# quicksort_v2
# Function Signature
python

def quicksort_v2(array: List[int]) -> List[int]:
    """
    Sorts the input list in-place using the 3-way partition QuickSort algorithm.

    Parameters:
    - array (List[int]): The list to be sorted.

    Returns:
    - List[int]: The sorted list.
    """
    ...

# Behavior
The quicksort_v2 function performs an in-place sort on the input list using the 3-way partition QuickSort algorithm. This algorithm efficiently handles duplicate elements, providing a balanced and optimized approach to sorting. It recursively partitions the input list into three segments based on a randomly selected pivot, rearranging elements to achieve the final sorted order.

# Attributes
array (List[int]): The list of integers to be sorted in-place.
# Returns
List[int]: The sorted list.
# Documentation
The quicksort_v2 function implements the 3-way partition QuickSort algorithm, which is known for its efficiency in handling lists with duplicate elements. The behavior of the function involves recursively partitioning the input list, selecting random pivots, and rearranging elements into three segments: those less than the pivot, those equal to the pivot, and those greater than the pivot.

# Explanation
   # Input List Modification:

The function modifies the input list (array) in-place, avoiding the need for additional memory usage during sorting.
   # Partitioning Process:

The input list is partitioned into three segments: elements less than the pivot, elements equal to the pivot, and elements greater than the pivot.
The pivot is randomly selected to ensure a balanced partitioning.
   # Recursive Sorting:

The function recursively applies the 3-way partitioning process to sublists until the entire list is sorted.
   # Handling Duplicate Elements:

Efficient handling of duplicate elements ensures the algorithm's suitability for scenarios where repeated values are present in the input list.
   # Return Value:

The function returns the same list object after sorting, now arranged in ascending order.


# Example
In-Place 3-Way Partition QuickSort
To use the in-place 3-way partition QuickSort, import the quicksort_v2 function and provide a list of integers to be sorted.
from quicksort import quicksort_v2
array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
sorted_array = quicksort_v2(array)
print("Sorted Array:", sorted_array)

