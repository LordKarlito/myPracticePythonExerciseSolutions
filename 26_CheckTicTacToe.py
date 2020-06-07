"""
This exercise is Part 2 of 4 of the tic tac toe exercise series. 

As you may have guessed, we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of coding, so we're doing it in pieces.

Today, we will simply focus on checking whether someone has WON a game of tic tac toe, not worrying about how the moves were made.

If a game of tic tac toe is represented as a list of lists, like so:

game = [[1,2,0],
        [2,1,0],
        [2,1,1]]

where a 0 means an empty square, a 1 means that player 1 put their token in that space, and a 2 means that player 2 put their token in that space.

Your task: Given a 3x3 list of lists that represents a tic tac toe game board, tell me whether anyone has won, and tell me which player won, if any. A tic tac toe win is 3 in a row - either in a row, a column, or a diagonal. Don't worry about the case where Two people have won - assume that in every board there will be only one winner.

Some examples

winner_is_2 = [[2, 2, 0],
        	   [2, 1, 0],
	           [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_also_1 = [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 2, 0],
	         [2, 1, 0],
	         [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]
"""

def checkColumns(board):
    for x in range(0,len(board[0])):
        if board[0][x] == board[1][x] and board[0][x] == board[2][x]:
            print("The winner is {}".format(board[0][x]))

def checkRows(board):
    for x in range(0,len(board[0])):
        if board[x][0] == board[x][1] and board[x][0] == board[x][2]:
            print("The winner is {}".format(board[x][0]))
            return(board[x][0])

def checkDiagonal(board):
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        print("The winner is {}".format(board[0][0]))
    elif board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        print("The winner is {}".format(board[0][2]))

def checkWinner(board):
    checkRows(board)
    checkColumns(board)
    checkDiagonal(board)

    # return("Winner: {}".format(winner))
board = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]
checkWinner(board)
