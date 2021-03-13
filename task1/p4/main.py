import math


def f(n):
    if n == 1 or n == 0:
        return 2
    return f(n - 1) ** 2 / 18 - math.cos(f(n - 1)) - 6


print('f({}) = {:.2e}'.format(11, f(11)))
print('f({}) = {:.2e}'.format(3, f(3)))
num = int(input())
print('f({}) = {:.2e}'.format(num, f(num)))
