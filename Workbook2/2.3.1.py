import pandas as pd
import numpy as np

a = pd.Series(np.array((1, 1, 1)))
b = pd.Series(np.array((2, 3, 4)))

print(np.sqrt(np.sum(np.square(a - b))))