import pandas as pd

teams = pd.DataFrame({
    "Team": ["CSK", "MI", "RCB", "GT"],
    "Won": [8, 7, 6, 9],
    "Lost": [4, 5, 6, 3]
})

teams["Points"] = teams["Won"] * 2

print(
    teams.sort_values("Points", ascending=False)
)