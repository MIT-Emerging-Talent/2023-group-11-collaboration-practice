These functions can be used to solve the staircase climbing problem with different approaches, allowing for flexibility in terms of time complexity and efficiency. Choose the appropriate function based on your specific requirements and constraints.

def count_ways_to_climb_basic
This function calculates the number of distinct ways to climb a staircase with a given number of steps using a basic recursive approach. The idea is to explore all possible combinations of taking 1, 2, or 3 steps at each recursive step.
Parameters:
num_steps (int): The total number of steps in the staircase.
Returns:
int: The total number of distinct ways to climb the staircase.

def count_ways_to_climb_memo
This function employs memoization to optimize the calculation of the number of distinct ways to climb a staircase. It avoids redundant recursive calls by storing and reusing previously computed results.

Parameters:
num_steps (int): The total number of steps in the staircase.
memo (dict, optional): A dictionary to store previously computed results for memoization.
Returns:
int: The total number of distinct ways to climb the staircase.

def count_ways_to_climb_table
This function utilizes dynamic programming with a bottom-up approach to efficiently calculate the number of distinct ways to climb a staircase. It uses a table to store intermediate results, avoiding redundant computations.

Parameters:
num_steps (int): The total number of steps in the staircase.
Returns:
int: The total number of distinct ways to climb the staircase.

