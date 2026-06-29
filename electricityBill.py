import pandas as pd

houses = pd.DataFrame({
    "House":["A","B","C","D"],
    "Units":[120,350,280,150]
})

houses["Bill"] = houses["Units"] * 7

houses.loc[houses["Units"] > 300,"Bill"] *= 1.10

print(houses)