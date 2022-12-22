"""
Tic Tac Toe Player
"""

import copy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xCount = 0
    oCount = 0

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == X:
                xCount += 1
            elif board[i][j] == O:
                oCount += 1
    
    if xCount > oCount:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleActions = set()

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                possibleActions.add((i, j))
            
    return possibleActions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    tempBoard = copy.deepcopy(board)

    if action not in actions(board):
        raise Exception("Invalid Action")

    tempBoard[action[0]][action[1]] = player(board)

    return tempBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Rows 
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        if board[0][0] is not None:
            return board[0][0]
    elif board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        if board[1][0] is not None:
            return board[1][0]
    elif board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        if board[2][0] is not None:
            return board[2][0]
    # Columns 
    elif board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        if board[0][0] is not None:
            return board[0][0]
    elif board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        if board[0][1] is not None:
            return board[0][1]
    elif board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        if board[0][2] is not None:
            return board[0][2]
    # Diagonals
    elif board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        if board[0][0] is not None:
            return board[0][0]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        if board[0][2] is not None:
            return board[0][2]
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True 

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] is None:
                return False

    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    if player(board) == X:
        value, move = maxValue(board)
        return move
    else:
        value, move = minValue(board)
        return move


def maxValue(board):

    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None 

    for action in actions(board):
        value, act = minValue(result(board, action))
        if value > v:
            v = value
            move = action
            if v == 1:
                return v, move

    return v, move


def minValue(board):

    if terminal(board):
        return utility(board), None
    
    v = float('inf')
    move = None

    for action in actions(board):
        value, act = maxValue(result(board, action))
        if value < v:
            v = value
            move = action
            if v == -1:
                return v, move

    return v, move

