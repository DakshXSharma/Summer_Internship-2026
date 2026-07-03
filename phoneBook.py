import pandas as pd

contacts = pd.DataFrame({
    "Name": ["Aman","Riya","Kunal"],
    "Phone": [9876543210,9123456780,9988776655]
})

while True:
    print("\n1.Show")
    print("2.Search")
    print("3.Exit")

    ch = input()

    if ch == "1":
        print(contacts)

    elif ch == "2":
        name = input("Name: ")

        print(
            contacts[
                contacts["Name"] == name
            ]
        )

    else:
        break