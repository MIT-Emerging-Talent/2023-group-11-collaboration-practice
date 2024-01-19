"""
Module: test_coin_change.py

This module contains unit tests for the coin change functions (coin_change_basic, coin_change_memo, coin_change_tab)
located in the 'coins' module.
"""


import unittest
import os
import sys 

# Update the path to include the directory containing your main file
file_dir = os.path.dirname(os.path.dirname(__file__))
sys.path.append(file_dir + "/src")

from coins import coin_change_basic, coin_change_memo, coin_change_tab


class TestCoinChangeBasic(unittest.TestCase):
    """
    Test cases for the coin_change_basic function.
    """
    
    def test_with_1(self):
        
        """
        Test coin_change_basic with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 1
        result = 1
        self.assertEqual(coin_change_basic(amount, coins), result)

    def test_with_7(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 7
        result = 3
        self.assertEqual(coin_change_basic(amount, coins), result)

    def test_with_10(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 10
        result = 2
        self.assertEqual(coin_change_basic(amount, coins), result)

    def test_with_12(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 12
        result = 4
        self.assertEqual(coin_change_basic(amount, coins), result)


class TestCoinChangeMemo(unittest.TestCase):
    def test_with_1(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        coins = [1, 3, 5]
        amount = 1
        result = 1
        self.assertEqual(coin_change_memo(amount, coins), result)

    def test_with_7(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 7
        result = 3
        self.assertEqual(coin_change_memo(amount, coins), result)

    def test_with_10(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 10
        result = 2
        self.assertEqual(coin_change_memo(amount, coins), result)

    def test_with_12(self):
        
        """
        Test coin_change_memo with a valid input scenario.
        """
        
        coins = [1, 3, 5]
        amount = 12
        result = 4
        self.assertEqual(coin_change_memo(amount, coins), result)


class TestCoinChangeTab(unittest.TestCase):
    def test_with_1(self):
        
        """
        Test coin_change_tab with a valid input scenario.
        """

        coins = [1, 3, 5]
        amount = 1
        result = 1
        self.assertEqual(coin_change_tab(amount, coins), result)

    def test_with_7(self):
        """
        Test coin_change_tab with a valid input scenario.
        """

        coins = [1, 3, 5]
        amount = 7
        result = 3
        self.assertEqual(coin_change_tab(amount, coins), result)

    def test_with_10(self):
        """
        Test coin_change_tab with a valid input scenario.
        """

        coins = [1, 3, 5]
        amount = 10
        result = 2
        self.assertEqual(coin_change_tab(amount, coins), result)

    def test_with_12(self):
        """
        Test coin_change_tab with a valid input scenario.
        """

        coins = [1, 3, 5]
        amount = 12
        result = 4
        self.assertEqual(coin_change_tab(amount, coins), result)


if __name__ == "__main__":
    unittest.main()
