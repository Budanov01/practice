import matplotlib.pyplot as plt
import sys
import math


def function_y(x):
    y = x ** 2 * math.sin(x)
    return y


def coordinates():  # this function returns coordinates of interpolated function
    new_x = list()
    new_y = list()
    try:
        a, b = input('Введите отрезок по x: a, b = ').split(', ')
        step_x = float(input('Введите шаг по x '))
        a = float(a)
        b = float(b)
        if step_x < 0:
            print('введено неправильно')
            sys.exit(1)
    except Exception:
        print('введено неправильно')
        sys.exit(1)
    while a <= b:
        new_x.append(a)
        a += step_x
    for x in new_x:
        new_y.append(function_y(x))
    return new_x, new_y


def dichotomy(a, b, epsilon):
    k = int(1)
    while b - a >= epsilon * 2:
        p = (a + b) / 2 - epsilon
        q = (a + b) / 2 + epsilon
        if function_y(p) > function_y(q):
            a = (a + b) / 2
        if function_y(p) < function_y(q):
            b = (a + b) / 2
        k += 1
    x = (a + b) / 2
    return x, function_y(x), k


def golden_ratio(a, b, epsilon):
    k = int(1)
    f = (math.sqrt(5) + 1) / 2

    while b - a >= epsilon * 2:
        c = a + (b - a) / f
        d = b - (b - a) / f
        if function_y(c) <= function_y(d):
            a = d
        if function_y(c) > function_y(d):
            b = c
        k += 1
    x = (a + b) / 2
    return x, function_y(x), k


def fibonacсiMethod(a, b, epsilon):
    f1 = int(1)
    f2 = int(1)
    numbers = [1, 1]
    N = (b - a) / epsilon

    i = 1
    while i == 1:
        f3 = f1 + f2
        numbers.append(f3)
        f1 = f2
        f2 = f3
        if numbers[-1] > N > numbers[-2]:
            i = 0

    number = len(numbers)
    l = (b - a) / numbers[-1]
    k = int(1)

    while k != number - 1:
        x_2 = a + l * numbers[number - k - 1]
        x_1 = b - l * numbers[number - k - 1]
        if function_y(x_1) > function_y(x_2):
            a = x_1
        elif function_y(x_1) <= function_y(x_2):
            b = x_2
        k += 1

    x = (a + b) / 2
    print(number, numbers)
    return x, function_y(x), k


x, y = coordinates()
plt.plot(x, y, '-')
plt.show()
a, b, epsilon = input('введите отрезо (a, b) и погрешность epsilon: a, b, epsilon = ').split(', ')
a, b, epsilon = float(a), float(b), float(epsilon)
x0, y0, k0 = dichotomy(a, b, epsilon)
x1, y_1, k1 = golden_ratio(a, b, epsilon)
x2, y2, k2 = fibonacсiMethod(a, b, epsilon)
print(
    '\nМетод дихотомии:\nЧисло итераций = ' + str(k0) + '\n Минимум f(x)= ' + str(y0) + ' в точке x= ' + str(x0) + '\n')
print('Метод золотого сечения:\nЧисло итераций = ' + str(k1) + '\n Минимум f(x)= ' + str(y_1) + ' в точке x= ' + str(
    x1) + '\n')
print('Метод Фибоначчи:\nЧисло итераций = ' + str(k2) + '\n Минимум f(x)= ' + str(y2) + ' в точке x= ' + str(x2) + '\n')
plt.plot(x, y, '-', x0, y0, '+r', x1, y_1, '+g', x2, y2, '+y')
plt.show()
