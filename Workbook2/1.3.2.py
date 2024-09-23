import numpy as np
matrix = np.arange(25).reshape(5,5)
matrix[1:] = matrix[0]
print(matrix)