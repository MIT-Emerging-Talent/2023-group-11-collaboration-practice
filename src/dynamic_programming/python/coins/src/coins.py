def coin_change_basic(amount, coins):
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
        - Returns float("inf") if it's not possible to make the given amount with the available coins.
    """
    if memo is None:
        memo = {}
    if amount < 0:
        return float("inf")
    if amount == 0:
        return 0
 
 
    if amount in memo:
        return memo[amount]
    min_coins = float("inf")
    for coin in coins:
        num_coins = coin_change_memo(amount - coin, coins, memo) + 1
        min_coins = min(min_coins, num_coins)
        memo[amount] = min_coins

    return memo[amount]


def coin_change_tab(amount, coins):
    table = [float("inf")] * (amount + 1)
    table[0] = 0
    for i in range(amount + 1):
        for coin in coins:
            if i >= coin:
                table[i] = min(table[i], table[i - coin] + 1)
    return table[amount]
