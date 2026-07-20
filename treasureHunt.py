import numpy as np
import random

board = np.full((5, 5), ".")

treasure_row = random.randint(0, 4)
treasure_col = random.randint(0, 4)

while True:

    print(board)

    row = int(input("Row (0-4): "))
    col = int(input("Col (0-4): "))

    if row == treasure_row and col == treasure_col:

        board[row][col] = "X"

        print("\nTreasure Found!")
        print(board)

        break

    else:

        board[row][col] = "*"

        print("No treasure here!")