def count_ways_to_climb_basic(num_steps):
    if num_steps < 0:
        return 0

    if num_steps == 0:
        return 1

    return (
        count_ways_to_climb_basic(num_steps - 3)
        + count_ways_to_climb_basic(num_steps - 2)
        + count_ways_to_climb_basic(num_steps - 1)
    )

def count_ways_to_climb_memo(num_steps, memo={}):
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