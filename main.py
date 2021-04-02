import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.stats import poisson

def get_Integer(a, b):
    Int = np.zeros(math.ceil(b - a))
    for i in range(0, math.ceil(b - a)):
        Int[i] = a + i
    return Int

def get_Puasson(x, num):
    y = np.zeros(num)
    for i in range(0, num):
        y[i] = ((10 ** x[i]) / (fact(x[i]))) * math.exp(-10)
    return y

def fact(x):
    if x==0:
        return 1
    if x>0 and x<=1:
        return x
    else:
        return fact(x - 1) * x

arr = {10, 50, 1000}

np.random.seed(300)

for i in arr:
    data = np.random.normal(size=i)

    step = 0.2
    num = math.ceil((max(data) - min(data)) / step)

    x = np.linspace(min(data) - 0.2, max(data) + 0.2, 10000)
    y = lambda x: (1 / np.sqrt(2 * np.pi)) * np.exp(-x * x / 2)

    plt.plot(x, y(x))

    plt.hist(data, bins=num, range=(min(data) - 0.2, max(data) + 0.2), density=True)
    plt.title("Нормальное распределение, n = " + str(i))
    plt.show()

for i in arr:
    data = np.random.standard_cauchy(size=i)

    step = 0.2
    num = math.ceil((max(data) - min(data)) / step)

    x = np.linspace(min(data) - 0.2, max(data) + 0.2, 10000)
    y = lambda x: (1 / np.pi) * (1 / (x * x + 1))

    plt.plot(x, y(x))

    plt.hist(data, bins=num, range=(min(data) - 0.2, max(data) + 0.2), density=True)
    plt.title("Стандартное распределение Коши, n = " + str(i))
    plt.show()

for i in arr:
    data = np.random.laplace(size=i)

    step = 0.2
    num = math.ceil((max(data) - min(data)) / step)

    x = np.linspace(min(data) - 0.2, max(data) + 0.2, 10000)
    y = lambda x: (1 / np.sqrt(2)) * np.exp(-np.sqrt(2) * np.fabs(x))

    plt.plot(x, y(x))

    plt.hist(data, bins=num, range=(min(data) - 0.2, max(data) + 0.2), density=True)
    plt.title("Распределение Лапласса, n = " + str(i))
    plt.show()

for i in arr:
    data = poisson.rvs(size=i, mu=10)

    step = 0.2
    num = math.ceil((max(data) - min(data)) / step)

    x = get_Integer(min(data), max(data))
    y = get_Puasson(x, math.ceil(max(data) - min(data)))

    plt.plot(x, y)

    plt.hist(data, bins=range(min(data), max(data)), range=(min(data) - 0.2, max(data) + 0.2), density=True, rwidth=20)
    plt.title("Распределение Пуассона, n = " + str(i))
    plt.show()

for i in arr:
    x = range(i)
    data = [np.random.uniform(-(3 ** 0.5), (3 ** 0.5)) for j in x]
    step = 0.2
    num = math.ceil((max(data) - min(data)) / step)

    x = [-(3 ** 0.5) - step, -(3 ** 0.5), (3 ** 0.5), (3 ** 0.5) + step]
    y = [0, 1 / (2 * 3 ** 0.5), 1 / (2 * 3 ** 0.5), 0]

    plt.plot(x, y)

    plt.hist(data, bins=num, range=(min(data) - 0.2, max(data) + 0.2), density=True)
    plt.title("Равномерное распределение, n = " + str(i))
    plt.show()
