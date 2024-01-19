class Fibonacci:
    """
    This class represents an approach to calculate Fibonacci number using a recursive approach with memoization
    """

    def __init__(self) -> None:
        """
        Initializes the Fibonacci object.
        """
        self.memo = {}

    def fib(self, n: int) -> int:
        """
        Calculates the nth Fibonacci number using a recursive approach with memoization.

        Parameters:
        - n (int): The index of the Fibonacci number to be calculated.

        Returns:
        - int: The nth Fibonacci number.
        """
        if n in self.memo:
            """
            Return memoized result if available.
            """
            return self.memo[n]

        if n == 0:
            """
            Return 0 if value is 0. It is a boundary case.
            """
            return 0

        elif n == 1:
            """
            Return 1 if value is 1. It is a boundary case.
            """
            return 1
        else:
            """
            Recursively calculate Fibonacci values for n-1 and n-2.
            Return Fibonacci number.
            """
            result = self.fib(n - 1) + self.fib(n - 2)

        """
        Recursively calculate Fibonacci values for n-1 and n-2.
        Return Fibonacci number.
        """
        self.memo[n] = result
        return result
