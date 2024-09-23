import math as m

def add(num1, num2):
    res = int(num1) + int(num2)
    return res


def sub(num1, num2):
    res = int(num1) - int(num2)
    return res


def div(num1, num2):
    res = int(num1) / int(num2)
    return res


def mult(num1, num2):
    res = int(num1) * int(num2)
    return res


def f_e(num1, num2):
    res = m.pow(m.e, int(num1) + int(num2))
    return res


def f_sin(num1, num2):
    res = m.sin(int(num1) + int(num2))
    return res


def f_cos(num1, num2):
    res = m.cos(int(num1) + int(num2))
    return res


def power(num1, num2):
    res = m.pow(int(num1), int(num2))
    return res

num1 = input("Введите значение первого числа: ")
num2 = input("Введите значение второго числа: ")

print("Выберите операцию:")
print("1. Сложение\n2. Вычитание\n3. Умножение\n4. Деление\n5. Функция e^(x+y)\n6. Синус(x+y)\n7. Косинус (x+y)\n8. x^y")

x = int(input("Введите номер операции: "))

if x == 1:
    print(add(num1, num2))
if x == 2:
    print(sub(num1, num2))
if x == 3:
    print(mult(num1, num2))
if x == 4:
    print(div(num1, num2))
if x == 5:
    print(f_e(num1, num2))
if x == 6:
    print(f_sin(num1, num2))
if x == 7:
    print(f_cos(num1, num2))
if x == 8:
    print(power(num1, num2))