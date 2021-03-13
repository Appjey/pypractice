import math


def f(x):
    if x < -1:
        return float(x ** 7 - math.tan(x))
    elif x >= 71:
        return float(42 * x ** 8 - x ** 7 / 53 + 93)
    else:
        return float(x ** 3 + math.cos(x))


num = int(input())
print('f({}) = {:.2e}'.format(num, f(num)))
