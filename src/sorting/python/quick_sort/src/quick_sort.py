import random
# Time complexity O(nlogn)
# in-place 2-way partition
def quicksort_v1(array):
    def _quicksort(array, start, stop):
        # Base case: if the sublist has 1 or 0 elements, it's already sorted
        if start < stop - 1:
           # Choose a random pivot and partition the sublist 
            pivot_index = partition(array, start, stop) 
             # Recursively sort the sublists on both sides of the pivot
            _quicksort(array, start, pivot_index)
            _quicksort(array, pivot_index + 1, stop)

    def partition(array, start, stop):
        # Randomly choose a pivot and move it to the end of the sublist
        pivot_index = random.randint(start, stop - 1)
        array[pivot_index], array[stop - 1] = array[stop - 1], array[pivot_index]
        pivot = array[stop - 1]

        # Initialize the pointer 'i' at the start of the sublist
        i = start
        # Iterate through the sublist and move elements smaller than the pivot to the left
        for j in range(start, stop - 1):
            if array[j] <= pivot:
                array[i], array[j] = array[j], array[i]
                i += 1

        # Iterate through the sublist and move elements smaller than the pivot to the left

        array[i], array[stop - 1] = array[stop - 1], array[i]
        return i
     # Call the recursive quicksort function on the entire array
    _quicksort(array, 0, len(array))
    return array


# Time complexity O(nlogn)
# in-place 3-way partition
def quicksort_v2(array):
    # Base case: if the sublist has 1 or 0 elements, it's already sorted
    def _quicksort(array, start, stop):

        if stop - start < 2:
            return
        # Perform 3-way partitioning and get the indices of the equal elements range
        lt, gt = partition(array, start, stop)
        #Recursively sort the sublists less than the pivot and greater than the pivot
        _quicksort(array, start, lt)
        _quicksort(array, gt, stop)

    def partition(array, start, stop):
        # Choose a random pivot and initialize pointers
        pivot_index = random.randint(start, stop - 1)
        pivot = array[pivot_index]

        # Initialize pointers
        lt, i, gt = start, start, stop
        # Iterate through the sublist and rearrange elements based on their relationship to the pivot
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
        # Return the indices marking the range of equal elements
        return lt, gt
    # Call the recursive quicksort function on the entire array
    _quicksort(array, 0, len(array))
    return array