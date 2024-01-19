def coin_change_basic(amount, coins):
    """
    Find the minimum number of coins needed to make a given amount using the available coins.

    Args:
        amount (int): The target amount.
        coins (list): List of available coin denominations.

    Returns:
        int: The minimum number of coins needed.
    """
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0
    return min((coin_change_basic(amount - coin, coins) + 1) for coin in coins)


def coin_change_memo(amount, coins, memo=None):
    """
    Find the minimum number of coins needed to make a given amount using the available coins (with memoization).

    Args:
        amount (int): The target amount.
        coins (list): List of available coin denominations.
        memo (dict, optional): Memoization dictionary. Defaults to None.

    Returns:
        int: The minimum number of coins needed.
    """
    if memo is None:
        memo = {}
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0
    if amount not in memo:
        memo[amount] = min(coin_change_memo(amount - coin, coins, memo) + 1 for coin in coins)
    return memo[amount]


def coin_change_tab(amount, coins):
    """
    Find the minimum number of coins needed to make a given amount using the available coins (using dynamic programming).

    Args:
        amount (int): The target amount.
        coins (list): List of available coin denominations.

    Returns:
        int: The minimum number of coins needed.
    """
    table = [float("inf")] * (amount + 1)
    table[0] = 0
    for i in range(1, amount + 1):
        table[i] = min(table[i - coin] + 1 for coin in coins if i >= coin)
    return table[amount]


