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


def move_right():

    global board

    board = np.fliplr(board)

    moved = move_left()

    board = np.fliplr(board)

    return moved


def move_up():

    global board

    board = board.T

    moved = move_left()

    board = board.T

    return moved


def move_down():

    global board

    board = board.T

    board = np.fliplr(board)

    moved = move_left()

    board = np.fliplr(board)

    board = board.T

    return moved


# Start Game
add_new_tile()
add_new_tile()


while True:

    print_board()

    print("\nW = Up")
    print("A = Left")
    print("S = Down")
    print("D = Right")
    print("Q = Quit")

    move = input("Move: ").lower()

    moved = False

    if move == "a":
        moved = move_left()

    elif move == "d":
        moved = move_right()

    elif move == "w":
        moved = move_up()

    elif move == "s":
        moved = move_down()

    elif move == "q":
        break

    if moved:
        add_new_tile()