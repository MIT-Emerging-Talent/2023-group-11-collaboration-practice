import os
import sys
import unittest

file = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file + "/src")

from fib import Fibonacci

fibonacci_instance = Fibonacci()


class TestFibonacci(unittest.TestCase):
    def test_fib_with_0(self):
        # Test Fibonacci sequence with value 0
        n = 0
        result = 0
        self.assertEqual(fibonacci_instance.fib(n), result)

    def test_fib_with_1(self):
        # Test Fibonacci sequence with value 1
        n = 1
        result = 1
        self.assertEqual(fibonacci_instance.fib(n), result)

    def test_fib_with_2(self):
        # Test Fibonacci sequence with value 2
        n = 2
        result = 1
        self.assertEqual(fibonacci_instance.fib(n), result)

    def test_fib_with_10(self):
        # Test Fibonacci sequence with value 10
        n = 10
        result = 55
        self.assertEqual(fibonacci_instance.fib(n), result)

    def test_fib_with_20(self):
        # Test Fibonacci sequence with value 20
        n = 20
        result = 6765
        self.assertEqual(fibonacci_instance.fib(n), result)


if __name__ == "__main__":
    unittest.main()
