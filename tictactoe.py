"""
Tic Tac Toe Player
"""

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
    count_char=0
    for i in board:
        for j in i:
            if j is not None:
                count_char+=1
    if (count_char<9):
        if (count_char%2==0):
            return X
        else:
            return O
    elif count_char==9:
        return "Game Over"
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    act=set()
    for i in range (len(board)):
        for j in range (len(board[i])):
            if board[i][j]==None:
                act.add((i,j))
    if not act:
        return "Game Over"
    return act
    #raise NotImplementedError


def result(board, action):
    import copy
    """
    Returns the board that results from making move (i, j) on the board
    """
    try:
        if len(action)!=2:
            raise Exception("Should be integer")
    except:
        new_board = copy.deepcopy(board)
        new_board[action[0]][action[1]] = player(board) 
        return new_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range (3):
        #row check
        if len(set(board[i]))==1 and (None not in set(board[i])):
            return board[i][0]
        #column check
        if board[0][i]==board[1][i]==board[2][i] and ( board[0][i] is not None) :
            return board[0][i]
        #diagonal check
        if (((board[0][0]==board[1][1]==board[2][2]) or (board[0][2]==board[1][1]==board[2][0])) and (board[1][1] is not None)):
            return board[1][1]
    else:
        return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        return False
    else:
        return True
    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board)=="X":
        return 1
    elif winner(board)=="O":
        return int(-1)
    else:
        return 0
    #raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    Uses Alpha-Beta Pruning for optimization.
    """

    def max_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None  # Return score and no move
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_val, _ = min_value(result(board, action), alpha, beta)  # Get score from min_value
            if min_val > v:
                v = min_val
                best_action = action
            alpha = max(alpha, v)
            if beta <= alpha:  # Beta Cutoff
                break
        return v, best_action  # Return both best score and action

    def min_value(board, alpha, beta):
        if terminal(board):
            return utility(board), None  # Return score and no move
        v = math.inf
        best_action = None
        for action in actions(board):
            max_val, _ = max_value(result(board, action), alpha, beta)  # Get score from max_value
            if max_val < v:
                v = max_val
                best_action = action
            beta = min(beta, v)
            if beta <= alpha:  # Alpha Cutoff
                break
        return v, best_action  # Return both best score and action

    current_player = player(board)
    
    if current_player == X:
        _, best_move = max_value(board, -math.inf, math.inf)  # Expect tuple (score, move)
    else:
        _, best_move = min_value(board, -math.inf, math.inf)  # Expect tuple (score, move)
    
    return best_move

    #raise NotImplementedError
