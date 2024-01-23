# Overview

This Python module contains the implementation of the minimax and find_best_move functions, essential components for applying the minimax algorithm in the tic-tac-toe game. This solution is designed to determine the optimal move for a player at any given state of the game, considering both the current and potential future states of the board.

# Solution Behavior

The minimax function evaluates all possible future game states and selects the move that maximizes the player's chances of winning.
find_best_move iterates over the current game board, using minimax to evaluate the most advantageous move for the current player.
The algorithm returns the coordinates of the best move if one is available; otherwise, it indicates a draw or end-game scenario.

# Strategies and Implementations

- Recursive Game State Evaluation: minimax uses a recursive approach to explore all possible game states, applying the minimax strategy to choose the optimal move.
- Player Maximization and Minimization: The function differentiates between maximizing and minimizing players, adjusting its strategy accordingly.
- Efficient Game State Analysis: The implementation includes checks for winning conditions and board fullness to terminate recursion early where possible.

# Parameters and Returns

- Board: The current state of the game board, represented as a 2D list.
- Depth: The current depth in the recursive tree.
- Is Maximizing: A boolean indicating whether the function is currently maximizing or minimizing.
- Player: Indicates which player's move is being evaluated.
- Returns: The function returns the best score that can be achieved from the current game state.

# Usage

To use the minimax algorithm in your tic-tac-toe game:

```Python
from minimax import find_best_move

board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

best_move = find_best_move(board, player)  # player is -1 or 1
```
# Testing

- Comprehensive Test Suite: Includes tests for various game states, such as empty board, partial games, and end-game scenarios.

- Automated Testing: To run the tests, use the following command:

```bash
python -m unittest test_minimax.py
```