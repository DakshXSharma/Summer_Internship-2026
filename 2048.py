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


def move_left():

    global board

    moved = False

    for i in range(SIZE):

        row = list(board[i])

        # Remove zeros
        row = [x for x in row if x != 0]

        # Merge same numbers
        j = 0

        while j < len(row) - 1:

            if row[j] == row[j + 1]:

                row[j] *= 2
                row.pop(j + 1)
                moved = True

            j += 1

        # Fill remaining spaces with zeros
        while len(row) < SIZE:
            row.append(0)

        if list(board[i]) != row:
            moved = True

        board[i] = row

    return moved


# Start Game
add_new_tile()
add_new_tile()


while True:

    print_board()

    print("\nA = Left")
    print("Q = Quit")

    move = input("Move: ").lower()

    if move == "q":
        break

    elif move == "a":

        if move_left():
            add_new_tile()