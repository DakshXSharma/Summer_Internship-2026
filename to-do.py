tasks = []

while True:
    print("\n1 Add")
    print("2 Show")
    print("3 Remove")
    print("4 Exit")

    choice = input("Choice: ")

    if choice == "1":
        task = input("Task: ")
        tasks.append(task)

    elif choice == "2":
        for i, task in enumerate(tasks):
            print(i, task)

    elif choice == "3":
        index = int(input("Index: "))
        tasks.pop(index)

    elif choice == "4":
        break