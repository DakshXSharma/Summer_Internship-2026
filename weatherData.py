import pandas as pd

weather = pd.DataFrame({
    "Day":["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
    "Temperature":[35,38,42,36,34,39,40],
    "Humidity":[60,55,45,70,65,50,48]
})

print(weather)

print("\nHottest Day")
print(weather.loc[weather["Temperature"].idxmax()])

print("\nAverage Temperature")
print(weather["Temperature"].mean())

print("\nDays Above 37°C")
print(weather[weather["Temperature"] > 37])

print("\nAverage Humidity")
print(weather["Humidity"].mean())