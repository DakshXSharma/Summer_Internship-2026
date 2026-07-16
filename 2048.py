import numpy as np
import random

SIZE = 4

# Create empty board
board = np.zeros((SIZE, SIZE), dtype=int)

score = 0
previous_board = None
previous_score = 0


def print_board():

    print("\nScore:", score)

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

                global score
                row[j] *= 2
                score += row[j]
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


def check_win():

    return np.any(board == 2048)


def game_over():

    if np.any(board == 0):
        return False

    for i in range(SIZE):
        for j in range(SIZE - 1):

            if board[i][j] == board[i][j + 1]:
                return False

    for i in range(SIZE - 1):
        for j in range(SIZE):

            if board[i][j] == board[i + 1][j]:
                return False

    return True


def restart():

    global board
    global score

    board = np.zeros((SIZE, SIZE), dtype=int)

    score = 0

    add_new_tile()
    add_new_tile()


def undo():

    global board
    global score

    global previous_board
    global previous_score

    if previous_board is not None:

        board = previous_board.copy()

        score = previous_score

        print("\nLast move undone.")

    else:

        print("\nNothing to undo.")


# Start Game
add_new_tile()
add_new_tile()


while True:

    print_board()

    print("\nW = Up")
    print("A = Left")
    print("S = Down")
    print("D = Right")
    print("R = Restart")
    print("Z = Undo")
    print("Q = Quit")

    move = input("Move: ").lower()

    previous_board = board.copy()
    previous_score = score

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

    if check_win():

        print_board()

        print("\n🎉 Congratulations!")
        print("You reached 2048!")

        break

    if game_over():

        print_board()

        print("\nGame Over!")

        break