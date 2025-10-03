import math

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize the game board
board = [EMPTY] * 9

# Print the board
def print_board(board):
    print()
    for i in range(3):
        row = board[3*i:3*i+3]
        print(" | ".join(cell if cell != EMPTY else str(3*i + j) for j, cell in enumerate(row)))
        if i < 2:
            print("---------")
    print()

# Check for a win
def check_winner(board, player):
    win_positions = [
        [0,1,2], [3,4,5], [6,7,8],  # rows
        [0,3,6], [1,4,7], [2,5,8],  # columns
        [0,4,8], [2,4,6]            # diagonals
    ]
    return any(all(board[i] == player for i in combo) for combo in win_positions)

# Check for draw
def is_draw(board):
    return EMPTY not in board and not check_winner(board, HUMAN) and not check_winner(board, AI)

# Evaluate the board
def evaluate(board):
    if check_winner(board, AI):
        return 1
    elif check_winner(board, HUMAN):
        return -1
    else:
        return 0

# Minimax algorithm
def minimax(board, is_maximizing):
    score = evaluate(board)
    if score != 0 or is_draw(board):
        return score

    if is_maximizing:
        best_score = -math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = AI
                value = minimax(board, False)
                board[i] = EMPTY
                best_score = max(best_score, value)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board[i] == EMPTY:
                board[i] = HUMAN
                value = minimax(board, True)
                board[i] = EMPTY
                best_score = min(best_score, value)
        return best_score

# Find the best move for AI
def find_best_move(board):
    best_val = -math.inf
    best_move = -1
    for i in range(9):
        if board[i] == EMPTY:
            board[i] = AI
            move_val = minimax(board, False)
            board[i] = EMPTY
            if move_val > best_val:
                best_val = move_val
                best_move = i
    return best_move

# Main game loop
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O', AI is 'X'.")
    print("Board positions are numbered from 0 to 8.")
   
    current_player = HUMAN  # Human starts first
    print_board(board)

    while True:
        if current_player == HUMAN:
            move = int(input("Enter your move (0-8): "))
            if board[move] != EMPTY:
                print("Invalid move. Try again.")
                continue
            board[move] = HUMAN
        else:
            print("AI is thinking...")
            move = find_best_move(board)
            board[move] = AI
            print(f"AI plays at position {move}")

        print_board(board)

        if check_winner(board, current_player):
            print(f"{'Human' if current_player == HUMAN else 'AI'} wins!")
            break
        elif is_draw(board):
            print("It's a draw!")
            break

        current_player = HUMAN if current_player == AI else AI

# Run the game
play_game()

	

