import math


def f13(n, m):
    p1 = 0
    p2 = 0
    for i in range(1, n + 1):
        p1 = math.fsum([pow(i, 7), -pow(i, 4) / 85, p1])
        p2 = math.fsum([pow(i, 2), i, p2])
    return math.fsum([64 * m * p1, p2])
