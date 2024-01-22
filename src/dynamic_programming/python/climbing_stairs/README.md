
# Climbing Stairs Challenge

This repository contains Python implementations for solving the "Climbing Stairs" challenge using different approaches. 
The challenge involves finding the number of ways to climb a staircase with a given number of steps.

## Behaviors

### `count_ways_to_climb_basic(num_steps)`

This function counts the number of ways to climb stairs using a basic recursive approach.

#### Parameters
- `num_steps` (int): The number of steps to climb.

#### Return Value
- Returns an integer representing the count of ways to climb the stairs.

### `count_ways_to_climb_memo(num_steps, memo={})`

This function counts the number of ways to climb stairs using memoization.

#### Parameters
- `num_steps` (int): The number of steps to climb.
- `memo` (dict): Memoization dictionary. Defaults to an empty dictionary.

#### Return Value
- Returns an integer representing the count of ways to climb the stairs.

### `count_ways_to_climb_table(num_steps)`

This function counts the number of ways to climb stairs using dynamic programming.

#### Parameters
- `num_steps` (int): The number of steps to climb.

#### Return Value
- Returns an integer representing the count of ways to climb the stairs.
