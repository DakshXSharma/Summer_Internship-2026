import pandas as pd

data = {
    "Product": ["Pen", "Book", "NoteBook", "Laptop"],
    "Sales": [100, 300, 150, 50000]
}

df = pd.DataFrame(data)

print(df)

print("\nTotal Sales:")
print(df["Sales"].sum())

print("\nAverage Sales:")
print(df["Sales"].mean())