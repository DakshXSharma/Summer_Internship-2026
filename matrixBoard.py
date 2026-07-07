import numpy as np

SIZE = 5

board = np.random.randint(1, 10, (SIZE, SIZE))

while True:

    print("\nCurrent Board\n")
    print(board)

    print("\n1. Rotate Left")
    print("2. Rotate Right")
    print("3. Flip Horizontal")
    print("4. Flip Vertical")
    print("5. Show Statistics")
    print("6. Generate New Board")
    print("7. Exit")

    choice = input("\nChoice: ")

    if choice == "1":

        board = np.rot90(board)

    elif choice == "2":

        board = np.rot90(board, -1)

    elif choice == "3":

        board = np.fliplr(board)

    elif choice == "4":

        board = np.flipud(board)

    elif choice == "5":

        print("\nMaximum :", np.max(board))
        print("Minimum :", np.min(board))
        print("Average :", round(np.mean(board),2))
        print("Sum :", np.sum(board))
        print("Even Numbers :", np.count_nonzero(board % 2 == 0))
        print("Odd Numbers :", np.count_nonzero(board % 2 != 0))

    elif choice == "6":

        board = np.random.randint(1,10,(SIZE,SIZE))

    elif choice == "7":

        break

    else:

        print("Invalid Choice")