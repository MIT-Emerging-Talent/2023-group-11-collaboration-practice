from typing import List

def array_product(nums: List[int]) -> List[int]:
    """
    Returns an array where each element is equal to the product of all elements in the input array,
    excluding the current one.

    Behavior:
    - For an empty array, the result is an empty array.
    - For an array with one element, the result is an array containing that element.
    - Assumes input elements are integers starting by 1.

    Parameter:
    - nums (List[int]): Input array of integers.

    Return value:
    - List[int]: Array where each element is the product of all elements in the input array, excluding the current one.

    Examples:
    >>> array_product([1, 2, 3, 4, 5])
    [120, 60, 40, 30, 24]

    >>> array_product([])
    []

    >>> array_product([1])
    [1]
    """
    if not nums:
        return []

    total_product = 1

    for num in nums:
        
        # return array with all zero, if only one num is zero
        if num == 0:
            return [0] * len(nums)
        
        total_product *= num

    result = [total_product // num for num in nums]
    return result




# Example usage:
my_array = [1, 2, 3, 4, 5]
result = array_product(my_array)
print("Array product: ", result)
