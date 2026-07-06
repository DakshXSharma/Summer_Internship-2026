import numpy as np

matrix = np.arange(1,17).reshape(4,4)

print("Original:")
print(matrix)

print("\n90 Degree Rotation:")
print(np.rot90(matrix))