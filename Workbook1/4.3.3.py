import matplotlib.pyplot as plt
import math as m
import numpy as np
lst = [m.fabs(m.cos(x*m.e**(m.cos(x)+m.log10(x+1)))) for x in range(10)]
plt.grid()
plt.plot(range(10), lst, c = 'g')
plt.fill_between(range(10), lst)
plt.show()
print(f'Площадь: {np.trapz(lst)}')