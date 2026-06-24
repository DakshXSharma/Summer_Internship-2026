import pandas as pd

players = pd.DataFrame({
    "Player": ["Virat", "Rohit", "Gill", "Hardik"],
    "Runs": [750, 620, 810, 400],
    "Matches": [15, 15, 15, 12]
})

players["Average"] = (
    players["Runs"] / players["Matches"]
)

print("\nPlayers")
print(players)

print("\nTop Scorer")
print(
    players.loc[
        players["Runs"].idxmax()
    ]
)

print("\nAverage Team Runs")
print(players["Runs"].mean())

print("\nPlayers Above 700 Runs")
print(
    players[
        players["Runs"] > 700
    ]
)