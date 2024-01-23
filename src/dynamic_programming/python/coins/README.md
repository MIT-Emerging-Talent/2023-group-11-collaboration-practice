# Coin Change Functions

This Python module provides three functions to solve the minimum coin change problem using different approaches.

## Functions

### `coin_change_basic(amount, coins)`

#### Description

Find the minimum number of coins needed to make a given amount using the available coins using a basic recursive approach.

#### Parameters

- `amount` (int): The target amount.
- `coins` (list): List of available coin denominations.

#### Returns

- `int`: The minimum number of coins needed.

### `coin_change_memo(amount, coins, memo=None)`

#### Description

Find the minimum number of coins needed to make a given amount using the available coins with memoization to improve efficiency.

#### Parameters

- `amount` (int): The target amount.
- `coins` (list): List of available coin denominations.
- `memo` (dict, optional): Memoization dictionary. Defaults to `None`.

#### Returns

- `int`: The minimum number of coins needed.

### `coin_change_tab(amount, coins)`

#### Description

Find the minimum number of coins needed to make a given amount using the available coins using dynamic programming and a table.

#### Parameters

- `amount` (int): The target amount.
- `coins` (list): List of available coin denominations.

#### Returns

- `int`: The minimum number of coins needed.


@@ The following comments are added by Murtaza @@

Coin Change Algorithms:
#coin_change_basic Function:

Purpose: Find the minimum number of coins needed for a given amount using available coin denominations.
Approach: Recursive exploration of all possible coin combinations.
Usage: coin_change_basic(amount, coins).

#coin_change_memo Function:
Purpose: Optimize the basic approach by using memoization to avoid redundant calculations.
Approach: Recursive function with memoization to store and reuse intermediate results.
Usage: coin_change_memo(amount, coins, memo=None).

#coin_change_tab Function:
Purpose: Utilize dynamic programming and tabulation (bottom-up) to find the minimum coins.
Approach: Build a table to store intermediate results and fill it in a bottom-up manner.
Usage: coin_change_tab(amount, coins).

#Testing:
The code includes a set of test cases written using the unittest framework to validate the correctness of the implemented functions.
Three test classes (TestCoinChangeBasic, TestCoinChangeMemo, and TestCoinChangeTab) cover various scenarios and edge cases for each algorithm.
The tests check if the functions produce the expected results for different coin denominations and target amounts.
