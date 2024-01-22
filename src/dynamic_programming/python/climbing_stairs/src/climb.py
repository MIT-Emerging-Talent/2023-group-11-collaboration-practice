__author__ = "Yanina Chukanova"
__date__ = "January 22, 2024"

def  count_ways_to_climb_basic(num_steps):
    """
    Count the number of ways to climb stairs using a recursive approach.

    Parameters:
    - num_steps (int): The number of steps to climb.

    Returns:
    - int: The count of ways to climb the stairs.
    """
    if num_steps < 0:
        return 0

    if num_steps == 0:
        return 1

    return (
         count_ways_to_climb_basic(num_steps - 3)
        + count_ways_to_climb_basic(num_steps - 2)
        +  count_ways_to_climb_basic(num_steps - 1)
    )

def count_ways_to_climb_memo(num_steps, memo={}):
    """
    Count the number of ways to climb stairs using memoization.

    Parameters:
    - num_steps (int): The number of steps to climb.
    - memo (dict): Memoization dictionary. Defaults to an empty dictionary.

    Returns:
    - int: The count of ways to climb the stairs.
    """
    if num_steps < 0:
        return 0

    if num_steps == 0:
        return 1

    if num_steps not in memo:
        memo[num_steps] = (
            count_ways_to_climb_memo(num_steps - 3, memo)
            + count_ways_to_climb_memo(num_steps - 2, memo)
            + count_ways_to_climb_memo(num_steps - 1, memo)
        )

    return memo[num_steps]

def count_ways_to_climb_table(num_steps):
    """
    Count the number of ways to climb stairs using dynamic programming.

    Parameters:
    - num_steps (int): The number of steps to climb.

    Returns:
    - int: The count of ways to climb the stairs.
    """
    if num_steps < 0:
        return 0

    if num_steps == 0:
        return 1

    table = [0] * (num_steps + 1)
    table[0] = 1

    for i in range(1, num_steps + 1):
        table[i] += table[i - 1]
        if i - 2 >= 0:
            table[i] += table[i - 2]
        if i - 3 >= 0:
            table[i] += table[i - 3]

    return table[num_steps]