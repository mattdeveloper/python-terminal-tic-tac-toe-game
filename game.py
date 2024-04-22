def print_board(board):
  for row in board:
    print("|" + "|".join(row) + "|")

print_board([["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]])