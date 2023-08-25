Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def is_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_draw(board):
    return all(cell != " " for row in board for cell in row)

def minimax(board, depth, maximizing_player):
    if is_winner(board, "X"):
        return -10 + depth
    elif is_winner(board, "O"):
        return 10 - depth
    elif is_draw(board):
        return 0

    if maximizing_player:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

def find_best_move(board):
    best_move = None
    best_eval = float("-inf")

    for i in range(3):
...         for j in range(3):
...             if board[i][j] == " ":
...                 board[i][j] = "O"
...                 move_eval = minimax(board, 0, False)
...                 board[i][j] = " "
...                 
...                 if move_eval > best_eval:
...                     best_eval = move_eval
...                     best_move = (i, j)
...     return best_move
... 
... def main():
...     board = [[" " for _ in range(3)] for _ in range(3)]
... 
...     print("Tic-Tac-Toe: You are X and AI is O")
...     print_board(board)
... 
...     while True:
...         row, col = map(int, input("Enter row and column (0-2) for your move: ").split())
...         if board[row][col] != " ":
...             print("Cell already occupied. Try again.")
...             continue
... 
...         board[row][col] = "X"
...         print_board(board)
... 
...         if is_winner(board, "X"):
...             print("You win!")
...             break
...         elif is_draw(board):
...             print("It's a draw!")
...             break
... 
...         ai_row, ai_col = find_best_move(board)
...         board[ai_row][ai_col] = "O"
...         print("AI's move:")
...         print_board(board)
... 
...         if is_winner(board, "O"):
...             print("AI wins!")
...             break
... 
... if __name__ == "__main__":
...     main()
