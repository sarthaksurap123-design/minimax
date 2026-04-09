# Tic-Tac-Toe using Minimax Algorithm

import math

# Initialize board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Print board
def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

# Check winner
def check_winner(board):
    # Rows & Columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != ' ':
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != ' ':
            return board[0][i]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Check if moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax function
def minimax(board, depth, is_max):
    winner = check_winner(board)

    # Terminal conditions
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif not is_moves_left(board):
        return 0

    # Maximizer
    if is_max:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, depth + 1, False))
                    board[i][j] = ' '
        return best

    # Minimizer
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, depth + 1, True))
                    board[i][j] = ' '
        return best

# Find best move
def find_best_move(board):
    best_val = -math.inf
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, 0, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Game loop
def play_game():
    print("Tic-Tac-Toe (You = O, AI = X)")
    print_board(board)

    while True:
        # User move
        x = int(input("Enter row (0-2): "))
        y = int(input("Enter col (0-2): "))

        if board[x][y] != ' ':
            print("Invalid move!")
            continue

        board[x][y] = 'O'
        print_board(board)

        if check_winner(board) == 'O':
            print("You win!")
            break
        if not is_moves_left(board):
            print("Draw!")
            break

        # AI move
        move = find_best_move(board)
        board[move[0]][move[1]] = 'X'
        print("AI Move:")
        print_board(board)

        if check_winner(board) == 'X':
            print("AI wins!")
            break
        if not is_moves_left(board):
            print("Draw!")
            break

# Run game
play_game()