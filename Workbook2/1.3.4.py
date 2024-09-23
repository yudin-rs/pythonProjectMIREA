import numpy as np
size = 3
matrix = np.zeros((size, size))
matrix[0:size:size-1]=1
matrix[1:size-1, :size:size-1] = 1
print(matrix)