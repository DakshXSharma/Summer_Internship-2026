import numpy as np
import random

SIZE = 3

board = np.full((SIZE, SIZE), ".")

treasure_row = random.randint(0, SIZE - 1)
treasure_col = random.randint(0, SIZE - 1)

while True:

    print(board)

    row = int(input(f"Row (0-{SIZE-1}): "))
    col = int(input(f"Col (0-{SIZE-1}): "))

    if row == treasure_row and col == treasure_col:

        board[row][col] = "X"

        print("\nTreasure Found!")
        print(board)

        break

    else:

        board[row][col] = "*"

        print("No treasure here!")