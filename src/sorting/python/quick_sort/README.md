Explanation:

The quicksort_v1 function initializes the quicksort process and then calls the recursive _quicksort function on the entire array.
The _quicksort function is the recursive part of the algorithm. It checks for the base case where the sublist has 1 or 0 elements (already sorted) and recursively calls itself on the sublists on both sides of the pivot.
The partition function chooses a random pivot, moves it to the end of the sublist, and then rearranges the elements based on their relationship to the pivot. It returns the index where the pivot is now located.
The algorithm continues partitioning and sorting until the base case is reached, resulting in a sorted array.
This implementation uses a random pivot to improve performance in certain cases. The pointer 'i' is used to keep track of the position where elements smaller than the pivot should be placed. The final result is an in-place 2-way partition quicksort algorithm with a time complexity of O(n log n).

Explanation:

The quicksort_v2 function initializes the quicksort process and then calls the recursive _quicksort function on the entire array.
The _quicksort function is the recursive part of the algorithm. It checks for the base case where the sublist has 1 or 0 elements (already sorted) and recursively calls itself on the sublists less than the pivot and greater than the pivot.
The partition function chooses a random pivot, initializes pointers, and then rearranges elements based on their relationship to the pivot. It returns the indices marking the range of equal elements.
The algorithm continues 3-way partitioning and sorting until the base case is reached, resulting in a sorted array.

This implementation uses a random pivot selection and performs an in-place 3-way partition. The partition function now returns two indices, lt and gt, representing the range of elements equal to the pivot. The recursive calls are then made for the ranges [start, lt) and [gt, stop).
This implementation is an in-place 3-way partition quicksort algorithm with a time complexity of O(n log n). It efficiently handles arrays with duplicate elements.