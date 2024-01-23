The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1. Given an integer n, the task is to find the nth number in the Fibonacci sequence.

# Fibonacci Solution

This project includes a Python solution for calculating Fibonacci numbers efficiently using one of the approaches.


## Approach

### 'Recursive Solution with Memoization'

The file `fibonacci_recursive_memo.py` contains a class `Fibonacci` with a method `fib` that calculates the nth Fibonacci number using a recursive approach with memoization. This approach significantly reduces redundant computations by storing previously calculated Fibonacci values in a memo dictionary.

To use this solution, create an instance of the `Fibonacci` class and call the `fib` method with the desired value of `n`.


#### Complexity

In this version, I added a dictionary self.memo to store previously computed Fibonacci values. Before making a recursive call, the function checks if the value for the current n is already in the memo dictionary. If it is, the function returns the memoized result instead of recalculating it.

This memoization technique significantly reduces redundant computations, making the algorithm more efficient. The time complexity is now O(n), as each Fibonacci value is computed only once and stored in the memo dictionary for future use.


##### How to Run Tests

The project includes unit tests for both Fibonacci solutions. To run the tests, follow these steps:

1. Navigate to the project directory in your terminal.
2. Run the following command to discover and execute all tests:

   ```bash
   python -m unittest discover
