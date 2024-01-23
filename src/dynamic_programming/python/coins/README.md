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

@@ The following explanation inserted by Murtaza @@

##Explanation of Coin Change Functions:
1. coin_change_basic Function:
Purpose: Find the minimum number of coins needed to make a given amount using available coins.
Approach: Recursive function exploring all possible coin combinations.
Usage: coin_change_basic(amount, coins).
2. coin_change_memo Function:
Purpose: Find the minimum number of coins needed with memoization for optimization.
Approach: Recursive function with memoization to avoid redundant calculations.
Usage: coin_change_memo(amount, coins, memo=None).
3. coin_change_tab Function:
Purpose: Find the minimum number of coins needed using dynamic programming and a table.
Approach: Tabulation (bottom-up) approach, filling a table to store intermediate results.
Usage: coin_change_tab(amount, coins).
Test Cases:
The provided test cases use the unittest framework to verify the correctness of the coin change functions.
Three test classes are defined: TestCoinChangeBasic, TestCoinChangeMemo, and TestCoinChangeTab.
Each test class contains multiple test methods, each testing a different scenario.
The tests cover cases with varying coin denominations and target amounts.
The expected results are asserted using self.assertEqual(actual_result, expected_result).