import math


def f(x):
    return math.sqrt((x ** 7 - (x ** 4 / 85)) / (x ** 3 + x ** 4)) - (x ** 4 - 53 * x ** 5 + 93) / (
            x ** 3 - math.log(x) + 11) + (math.sin(x) + math.sin(x)) / (math.cos(x) + x ** 3)


num = int(input())
print('f({}) = {:.2e}'.format(num, f(num)))
