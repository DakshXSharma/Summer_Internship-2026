import pandas as pd

cars = pd.DataFrame({
    "Car":["A","B","C","D"],
    "Distance":[450,600,700,550],
    "Fuel":[30,40,42,35]
})

cars["Mileage"] = (
    cars["Distance"] /
    cars["Fuel"]
)

print(cars)

print("\nBest Mileage")

print(cars.loc[
    cars["Mileage"].idxmax()
])