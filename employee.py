import pandas as pd

employees = pd.DataFrame({
    "Name": ["Aman", "Riya", "Kunal", "Neha"],
    "Present": [22, 18, 25, 20],
    "WorkingDays": [25, 25, 25, 25]
})

employees["Attendance %"] = (
    employees["Present"] /
    employees["WorkingDays"]
) * 100

print(employees)

print("\nAbove 80% Attendance")
print(employees[employees["Attendance %"] >= 80])