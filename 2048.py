import numpy as np
import random

SIZE = 4

# Create empty board
board = np.zeros((SIZE, SIZE), dtype=int)


def print_board():

    print("\n---------------------")

    for row in board:
        for num in row:

            if num == 0:
                print(".", end="\t")

            else:
                print(num, end="\t")

        print()

    print("---------------------")


def add_new_tile():

    empty = []

    for i in range(SIZE):
        for j in range(SIZE):

            if board[i][j] == 0:
                empty.append((i, j))

    if len(empty) == 0:
        return

    row, col = random.choice(empty)

    if random.random() < 0.9:
        board[row][col] = 2
    else:
        board[row][col] = 4


# Start Game
add_new_tile()
add_new_tile()

while True:

    print_board()

    move = input(
        "\nPress Enter for next tile (q to quit): "
    )

    if move.lower() == "q":
        break

    add_new_tile()