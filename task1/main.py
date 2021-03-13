from К25 import tests
import math


def f11(x):
    x = int(x[0])
    return math.sqrt((x ** 7 - (x ** 4 / 85)) / (x ** 3 + x ** 4)) - (x ** 4 - 53 * x ** 5 + 93) / (
            x ** 3 - math.log(x) + 11) + (math.sin(x) + math.sin(x)) / (math.cos(x) + x ** 3)


def f12(x):
    x = int(x[0])
    if x < -1:
        return float(x ** 7 - math.tan(x))
    elif x >= 71:
        return float(42 * x ** 8 - x ** 7 / 53 + 93)
    else:
        return float(x ** 3 + math.cos(x))


def f13(n, m):
    p1 = 0
    p2 = 0
    for i in range(1, n + 1):
        p1 = math.fsum([pow(i, 7), -pow(i, 4) / 85, p1])
        p2 = math.fsum([pow(i, 2), i, p2])
    return math.fsum([64 * m * p1, p2])


def f14(n):
    if n == 1 or n == 0:
        return 2
    return f14(n - 1) ** 2 / 18 - math.cos(f14(n - 1)) - 6


assert f11(tests.get("f11")[11][0][0]) == tests.get("f11")[11][0][1], "error f11"
assert f11(tests.get("f11")[11][1][0]) == tests.get("f11")[11][1][1], "error f11"
assert f11(tests.get("f11")[11][2][0]) == tests.get("f11")[11][2][1], "error f11"
assert f11(tests.get("f11")[11][3][0]) == tests.get("f11")[11][3][1], "error f11"
assert f11(tests.get("f11")[11][4][0]) == tests.get("f11")[11][4][1], "error f11"

assert f12(tests.get("f12")[11][0][0]) == tests.get("f12")[11][0][1], "error f12"
assert f12(tests.get("f12")[11][1][0]) == tests.get("f12")[11][1][1], "error f12"
assert f12(tests.get("f12")[11][2][0]) == tests.get("f12")[11][2][1], "error f12"
assert f12(tests.get("f12")[11][3][0]) == tests.get("f12")[11][3][1], "error f12"
assert f12(tests.get("f12")[11][4][0]) == tests.get("f12")[11][4][1], "error f12"

print(f13(tests.get("f13")[11][1][0][0], tests.get("f13")[11][1][0][1]))
print(tests.get("f13")[11][1][1])
assert f13(tests.get("f13")[11][0][0][0], tests.get("f13")[11][0][0][1]) == tests.get("f13")[11][0][1], "error f13"
assert f13(tests.get("f13")[11][1][0][0], tests.get("f13")[11][1][0][1]) == tests.get("f13")[11][1][1], "error f13"
assert f13(tests.get("f13")[11][2][0][0], tests.get("f13")[11][2][0][1]) == tests.get("f13")[11][2][1], "error f13"
assert f13(tests.get("f13")[11][3][0][0], tests.get("f13")[11][3][0][1]) == tests.get("f13")[11][3][1], "error f13"
assert f13(tests.get("f13")[11][4][0][0], tests.get("f13")[11][4][0][1]) == tests.get("f13")[11][4][1], "error f13"

"""
assert f14(tests.get("f14")[11][0][0]) == tests.get("f14")[11][0][1], "error f14"
assert f14(tests.get("f14")[11][1][0]) == tests.get("f14")[11][1][1], "error f14"
assert f14(tests.get("f14")[11][2][0]) == tests.get("f14")[11][2][1], "error f14"
assert f14(tests.get("f14")[11][3][0]) == tests.get("f14")[11][3][1], "error f14"
assert f14(tests.get("f14")[11][4][0]) == tests.get("f14")[11][4][1], "error f14"
"""
print("pass")
