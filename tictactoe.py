"""
Tic Tac Toe Player
"""

import math
import copy
import sys

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
   
    nofx = 0
    nofy = 0
    for i in board:
        for j in i:
            if j == X:
                nofx += 1
            if j == O:
                nofy += 1
    if nofx == nofy:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    
    acti = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                acti.add((i, j))
        
    return acti

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    deepco = copy.deepcopy(board)
    
    a = action[0]
    b = action[1]
    
    if deepco[a][b] != EMPTY:
        print("result exception")
        raise Exception("result exception")
        
        
    deepco[a][b] = player(board)
    return deepco
    
def threeEqual(lis):
    if lis[0] != EMPTY and lis[0] == lis[1] and lis[1] == lis[2]:
       return True
    
    return False
    
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
   
    for i in board:
       if threeEqual(i):
           return i[0]
           
    for m in range(3):
        lisv = [0, 0, 0]
        for n in range(3):
            lisv[n] = board[n][m]
        if threeEqual(lisv):
            return lisv[0]
            
    lisd1 = [board[0][0], board[1][1], board[2][2]]
    lisd2 = [board[0][2], board[1][1], board[2][0]]
    
    if threeEqual(lisd1):
        return lisd1[0]
    
    if threeEqual(lisd2):
        return lisd2[0]
        
    return None
    
def allCellsFilled(board):
    for i in board:
        for j in i:
            if j == EMPTY:
                return False
    return True
    
                
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    if winner(board) == X or winner(board) == O or allCellsFilled(board):
        return True
    return False

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0
    
    
alpha = float('-inf')
beta = float('inf')


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
   
    if terminal(board):
        return None
        
    currentPlayer = player(board)
    if currentPlayer == X:
        v = maxValue(board, alpha, beta)
        for action in actions(board):
            move = minValue(result(board, action), alpha, beta)
            if move == v:
                bestMove = action
        
    if currentPlayer == O:
        v = float('inf')
        for action in actions(board):
            move = maxValue(result(board, action), alpha, beta)
            if move < v:
                v = move
                bestMove = action
                
    
    return bestMove
   

def minValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('inf')
    for a in actions(board):
        v = min(v, maxValue(result(board, a), alpha, beta))
        beta = min(v, beta)
        print(beta)
        if alpha > beta:
            break
    return v
    
    
def maxValue(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = float('-inf')
    for a in actions(board):
        v = max(v, minValue(result(board, a), alpha, beta))
        alpha = max(v, alpha)
        print(alpha)
        if alpha > beta:
            break
    return v
    
    
            

