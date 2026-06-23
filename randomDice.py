import numpy as np

rolls = np.random.randint(1, 7, 100)

print("All Rolls:")
print(rolls)

print("\nAverage:")
print(np.mean(rolls))

print("\nMaximum:")
print(np.max(rolls))