# module_all_permutation.py

__author__ = "Yanina Chukanova"

__date__ = "January 20, 2024"

# This module provides functions for generating permutations of lists.all_permutations Function
all_permutations
Function Signature
python

def all_permutations(elements: List) -> Generator[List, None, None]:
    """
    Generate all permutations of the input elements.

    Parameters:
    - elements (List): The list of elements to generate permutations for.

    Yields:
    - List: A permutation of the input elements.
    """
    ...
## Documentation
The all_permutations function generates all permutations of the input list of elements using a recursive approach. It employs a yield statement to efficiently produce permutations one by one. The function handles the base case where the length of the input list is less than or equal to 1, in which case it yields the input elements as is. For larger lists, it recursively generates permutations by fixing each element at the first position and permuting the remaining elements.
## Behavior Description:

The all_permutations function generates all permutations of a given list of elements using a recursive approach. It employs a yield statement to produce permutations incrementally, making it memory-efficient for large input lists.

## Parameter Description:

elements: A list of elements for which permutations are to be generated.

## Return Value Description:
The function utilizes the yield statement to produce permutations incrementally.
Each permutation is generated as a list.

## Assumptions:

The function assumes that the input (elements) is a list.
It handles empty input lists and returns an empty list as the result.
The function is designed to work for any iterable, not just strings or lists.

# perm Function
## Function Signature
python

def perm(start: List, end: List = []) -> None:
    """
    Print all permutations of the input list.

    Parameters:
    - start (List): The list for which permutations are to be printed.
    - end (List): The current permutation being generated. Default is an empty list.

    Returns:
    - None
    """
    ...
## Documentation
The perm function prints all permutations of the input list using a recursive approach. It takes two parameters - start represents the list for which permutations are to be printed, and end represents the current permutation being generated. The base case of the recursion is when the length of start becomes 0, at which point the current permutation is printed.

## Behavior Description:

The perm function generates all permutations of a given list of elements using a recursive approach. It prints each permutation as it is generated.

## Parameter Description:

start: The list for which permutations are to be generated.
end: (Optional) A list that accumulates the current permutation during the recursive calls.
## Return Value Description:
The function does not explicitly return a value. It prints each permutation as a side effect.

## Assumptions:
The function assumes that the input (start) is a list.
It handles empty input lists and prints an empty list as the result.


# permutation Function
  ## Function Signature
python
def permutation(lst: List) -> List[List]:
    """
    Find all permutations of the given list.

    Parameters:
    - lst (List): The list for which permutations are to be found.

    Returns:
    - List[List]: A list containing all permutations of the input list.
    """
    ...
## Documentation
The permutation function finds all permutations of the given list using a recursive approach. It handles the base cases where the length of the input list is either 0 or 1. For lists with more than one element, the function iterates through the input list, fixing each element as the first element and recursively finding permutations of the remaining elements. The result is a list containing all permutations of the input list.
## Behavior Description:
The permutation function generates all permutations of a given list of elements using a recursive approach. It returns a list containing all the permutations.

## Parameter Description:
lst: A list of elements for which permutations are to be generated.
## Return Value Description:
The function returns a list containing all permutations.
Each permutation is represented as a list.

## Assumptions:
The function assumes that the input (lst) is a list.
It handles empty input lists and returns an empty list as the result.



