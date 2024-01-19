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
