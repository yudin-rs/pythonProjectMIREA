n = int(input("Введите размер массива: "))
array = []
for i in range(n):
    x = int(input("Введите элемент массива: "))
    array.append(x)

elem = [array[j] for j in range(0, n, 2)]
elem.reverse()
for k in range(0, n, 2):
    array[k] = elem[k // 2]
print(array)