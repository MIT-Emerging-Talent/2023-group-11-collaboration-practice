# src/merge_sort.py

def mergesort_v1(array):
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort each half
    left_half = mergesort_v1(left_half)
    right_half = mergesort_v1(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)

def mergesort_v2(array):
    if len(array) <= 1:
        return array

    # Split the array into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # Recursively sort each half
    left_half = mergesort_v2(left_half)
    right_half = mergesort_v2(right_half)

    # Merge the sorted halves using a more concise approach
    return sorted(left_half + right_half)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
