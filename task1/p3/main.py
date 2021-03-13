import math


def f(n, m):
    p1 = 0.0
    p2 = 0.0
    for i in range(1, n + 1):
        p1 += float(i ** 7 - float(i ** 4) / 85.0)
        p2 += float(i ** 2 + i)
    return float(64 * p1 * (m) + p2)


print('f({},{}) = {:.18e}'.format(68, 87, f(68, 87)))

assert f(68, 87) == 3.372234827763188e+17, "wrong"
print("OK")
