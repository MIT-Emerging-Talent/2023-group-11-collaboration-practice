def all_permutations(elements):
    """
    Generate all permutations of the input elements.

    Parameters:
    - elements (List): The list of elements to generate permutations for.

    Yields:
    - List: A permutation of the input elements.
    """
    if len(elements) <= 1:
        yield elements
        return
    for perm in all_permutations(elements[1:]):
        for i in range(len(elements)):
            # nb elements[0:1] works in both string and list contexts
            yield perm[:i] + elements[0:1] + perm[i:]
            
            
def perm(start, end=[]):
    """
    Print all permutations of the input list.

    Parameters:
    - start (List): The list for which permutations are to be printed.
    - end (List): The current permutation being generated. Default is an empty list.

    Returns:
    - None
    """
    if(len(start) == 0):
        print(end)
    else:
        for i in range(len(start)):
            perm(start[:i] + start[i+1:], end + start[i:i+1])         
            
# Python function to print permutations of a given list
def permutation(lst):
    """
    Find all permutations of the given list.

    Parameters:
    - lst (List): The list for which permutations are to be found.

    Returns:
    - List[List]: A list containing all permutations of the input list.
    """
    # If lst is empty then there are no permutations
    if len(lst) == 0:
        return []
 
    # If there is only one element in lst then, only
    # one permutation is possible
    if len(lst) == 1:
        return [lst]
 
    # Find the permutations for lst if there are
    # more than 1 characters
 
    l = [] # empty list that will store current permutation
 
    # Iterate the input(lst) and calculate the permutation
    for i in range(len(lst)):
       m = lst[i]
 
       # Extract lst[i] or m from the list.  remLst is
       # remaining list
       remLst = lst[:i] + lst[i+1:]
 
       # Generating all permutations where m is first
       # element
       for p in permutation(remLst):
           l.append([m] + p)
    return l