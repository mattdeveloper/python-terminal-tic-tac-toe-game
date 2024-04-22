def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as 'row,col': ")
            row, col = map(int, move.split(","))
            if (
                row >= 1
                and row <= 3
                and col >= 1
                and col <= 3
                and board[row - 1][col - 1] == " "
            ):
                board[row - 1][col - 1] = player
                break
            else:
                print("Invalid move. Please try again.")
        except ValueError:
            print(
                "Invalid input. Please enter row and column as 'row,col' (e.g., 2,3)."
            )
        except IndexError:
            print("Invalid input. Row and column must be between 1 and 3.")


def print_board(board):
    for row in board:
        print("|" + "|".join(row) + "|")


# Testing
board = [[" " for _ in range(3)] for _ in range(3)]
print_board(board)
player_move(board, "X")
print_board(board)
