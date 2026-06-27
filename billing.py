import pandas as pd

products = pd.DataFrame({
    "Item":["Milk","Rice","Soap","Bread"],
    "Price":[60,250,40,35]
})

bill = []

while True:

    print(products)

    item = input("\nEnter Item (exit to stop): ")

    if item == "exit":
        break

    quantity = int(input("Quantity: "))

    row = products[products["Item"] == item]

    if len(row) > 0:

        price = row.iloc[0]["Price"]

        bill.append({
            "Item": item,
            "Qty": quantity,
            "Total": price * quantity
        })

invoice = pd.DataFrame(bill)

print("\nInvoice")
print(invoice)

print("\nGrand Total")
print(invoice["Total"].sum())