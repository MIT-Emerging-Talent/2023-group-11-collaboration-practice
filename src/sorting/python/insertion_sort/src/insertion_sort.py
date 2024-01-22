def insertionsort_v2(arr):
    """
    Perform insertion sort on the input array.

    Parameters:
    - arr (list): The input array to be sorted.

    Returns:
    - list: The sorted array.

    Examples:
    >>> insertionsort_v2([3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5])
    [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]

    >>> insertionsort_v2(['banana', 'apple', 'orange', 'grape'])
    ['apple', 'banana', 'grape', 'orange']
    """
    for i in range(len(arr)):
        current_value = arr[i]
        position = i

        while position > 0 and arr[position - 1] > current_value:
            arr[position] = arr[position - 1]
            position -= 1

        arr[position] = current_value

    return arr


# Additional Test Cases
def test_insertionsort_v2():
    assert insertionsort_v2([]) == []
    assert insertionsort_v2([1]) == [1]
    assert insertionsort_v2([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert insertionsort_v2([2, 5, 1, 4, 3]) == [1, 2, 3, 4, 5]
    assert insertionsort_v2(['banana', 'apple', 'orange', 'grape']) == ['apple', 'banana', 'grape', 'orange']

if __name__ == "__main__":
    test_insertionsort_v2()
    print("All tests passed!")
