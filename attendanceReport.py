import pandas as pd

df = pd.DataFrame({
    "Student": ["Aman", "Riya", "Kunal", "Priya"],
    "Attendance": [92, 68, 80, 55]
})

print(df)

print("\nBelow 75% Attendance:")
print(df[df["Attendance"] < 75])