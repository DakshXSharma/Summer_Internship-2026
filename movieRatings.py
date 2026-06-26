import pandas as pd

movies = pd.DataFrame({
    "Movie": ["A", "B", "C", "D"],
    "Rating": [8.5, 7.2, 9.1, 6.8]
})

print(movies)

print("\nTop Rated:")
print(movies.sort_values(by="Rating", ascending=False))

print("\nRating Above 8:")
print(movies[movies["Rating"] > 8])