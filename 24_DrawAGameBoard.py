"""
Exercise 24 - Draw A Game Board
Level - X X

This exercise is part 1 of 4 of the tic tac toe exercise series

Time for some fake graphics! Let's say we want to draw game board that look like this

 --- --- ---
|   |   |   |
 --- --- --- 
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---

This one is 3x3 (like in tic-tac-toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python's print statement.
"""

# Function to make board. Contains other functions calls
def makeBoard(size):
    board = ""

    # 
    for x in range(size):
        board = makeRow(board, size)
        board = makeColumn(board, size)
    board = makeRow(board,size)
    return(board)


# Function to make rows
def makeRow(board, size):
    for x in range(size):
        board += " ---"
    return(board)

# Function to make columns
def makeColumn(board, size):
    board += "\n"
    for x in (range(size+1)):
        board += "|   "
    board += "\n"
    return(board)

size = int(input("Enter the size of the board(n x n): "))

print(makeBoard(size))