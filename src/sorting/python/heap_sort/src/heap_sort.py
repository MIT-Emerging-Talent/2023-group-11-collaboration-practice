from typing import List

def heap_sort(arr: List[int]) -> List[int]:
    """
    Sorts the input array in ascending order using the Heap Sort algorithm.

    Behavior:
    - For an empty array, the result is an empty array.
    - Returns the input array with a single element unchanged.
    - Sorts the input array in ascending order.
    - Sorts the input array in ascending order, even if the input is in decreasing order.
    - Sorts the input array in ascending order.

    Parameter:
    - arr (List[int]): Input array of integers.

    Return value:
    - List[int]: Sorted array in ascending order.

    Examples:
    >>> heap_sort([])
    []

    >>> heap_sort([1])
    [1]

    >>> heap_sort([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]

    >>> heap_sort([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]

    >>> heap_sort([2, 5, 1, 4, 3])
    [1, 2, 3, 4, 5]
    """
    def heapify(arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[left_child] > arr[largest]:
            largest = left_child

        if right_child < n and arr[right_child] > arr[largest]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    def build_max_heap(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

    if not arr:
        return []

    n = len(arr)

    build_max_heap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


# Example usage:
my_array = [2, 5, 1, 4, 8]
sorted_array = heap_sort(my_array)
print("Sorted array: ", sorted_array)
