import matplotlib.pyplot as plt
import math as m

array = [(m.sqrt(1+m.e**m.sqrt(x)+m.cos(x**2))/m.fabs(1-m.sin(x)**3)) + m.log10(2*x) for x in range(1,11)]
plt.plot(range(1,11), array, 'r-.')
plt.show()
plt.scatter(range(1, 6), array[:5])
plt.show()