import numpy as np
from matplotlib import pyplot as plt

np.random.seed(0)
size = 100
random_values = np.random.rand(size)

mean_value = np.mean(random_values)
median_value = np.median(random_values)

if mean_value > median_value:
    print("Среднее значение больше медианного.")
elif mean_value < median_value:
    print("Среднее значение меньше медианного.")
else:
    print("Среднее значение равно медианному.")

plt.scatter(range(size), random_values, color='blue')
plt.axhline(y=mean_value, color='red', linestyle='--', label='Среднее значение')
plt.axhline(y=median_value, color='green', linestyle='--', label='Медианное значение')
plt.title("Точечная диаграмма рассеяния случайных значений")
plt.xlabel("Индекс")
plt.ylabel("Значение")
plt.legend()
plt.show()
