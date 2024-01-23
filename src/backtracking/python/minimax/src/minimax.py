"""
Module: minimax

This module provides a minimax algorithm implementation for use in games like tic-tac-toe.
It includes functions for evaluating the best move in a given game state.

Functions:
    minimax(board, depth, is_maximizing, player): Evaluates and returns the best score for a given game state.
    find_best_move(board, player): Determines the best move for a player in a given game state.
"""

def minimax(board, depth, is_maximizing, player):
    """
    Evaluate the best score for a given game state using the minimax algorithm.

    Parameters:
    board (list): The game board as a list of lists.
    depth (int): The current depth in the game tree.
    is_maximizing (bool): True if the current move is by the maximizing player, False otherwise.
    player (int): The player (-1 or 1) for whom the best move is being calculated.

    Returns:
    int: The best score that can be achieved from the current game state.
    """
    def check_winner(b):
        for i in range(3):
            if b[i][0] == b[i][1] == b[i][2] != 0:
                return b[i][0]
            if b[0][i] == b[1][i] == b[2][i] != 0:
                return b[0][i]
        if b[0][0] == b[1][1] == b[2][2] != 0 or b[0][2] == b[1][1] == b[2][0] != 0:
            return b[1][1]
        return 0

    def is_board_full(b):
        return all(b[i][j] != 0 for i in range(3) for j in range(3))

    winner = check_winner(board)
    if winner != 0:
        return winner * player
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = player
                    score = minimax(board, depth + 1, False, player)
                    board[i][j] = 0
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = -player
                    score = minimax(board, depth + 1, True, player)
                    board[i][j] = 0
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board, player):
    """
    Determine the best move for a player in a given game state.

    Parameters:
    board (list): The game board as a list of lists.
    player (int): The player (-1 or 1) for whom the best move is being calculated.

    Returns:
    tuple: The coordinates (row, column) of the best move, or None if no moves are available.
    """
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                board[i][j] = player
                score = minimax(board, 0, False, player)
                board[i][j] = 0
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move

# Usage example
test_board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]
test_player = -1
print(find_best_move(test_board, test_player)) # Expected: (0, 0) or any other empty cell as the board is empty
