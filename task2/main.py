from К25 import tests


def f21(arg):
    if arg[3] == 'e':
        if arg[0] == 'ini':
            if arg[2] == 'rexx':
                return 0 if arg[1] == 2010 else 1 if arg[1] == 1963 else 2 if arg[1] == 1974 else None
            elif arg[2] == 'text':
                return 3 if arg[1] == 2010 else 4 if arg[1] == 1963 else 5 if arg[1] == 1974 else None
        elif arg[0] == 'jsx':
            if arg[2] == 'rexx':
                return 6
            elif arg[2] == 'text':
                return 7 if arg[4] == 1974 else 8 if arg[4] == 1968 else None
            else:
                return None
        else:
            return None
    elif arg[3] == 'julia':
        return 9
    else:
        return None


def f22(x):
    a = 0b1 & int(x)
    b = 0b11111111 << 1 & int(x)
    c = 0b11111111 << 9 & int(x)
    d = 0b1111111111 << 17 & int(x)
    e = 0b11111 << 27 & int(x)
    return int(hex(b << 23 | d >> 3 | a << 13 | c >> 4 | e >> 27), 16)


def f23(a):
    b = []
    c = []
    count = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(1, len(a[i]) - j):
                if a[i][j] == a[i][j + k]:
                    a[i][j + k] = None
            if a[i][j] is not None:
                c.insert(j, a[i][j])
        if c:
            b.append(c)
        c = []
    count *= 0
    for i in range(len(b)):
        for j in range(len(b[i])):
            b[i][j] = "да" if b[i][j] == '1' else "нет" if b[i][j] == '0' else b[i][j].split("@")[-1]
            if b[i][j].isdigit():
                b[i][j] = b[i][j][3:6] + "-" + b[i][j][6:8] + "-" + b[i][j][8:10]
    return b


assert f21(tests.get("f21")[11][0][0]) == tests.get("f21")[11][0][1], "error f21"
assert f21(tests.get("f21")[11][1][0]) == tests.get("f21")[11][1][1], "error f21"
assert f21(tests.get("f21")[11][2][0]) == tests.get("f21")[11][2][1], "error f21"
assert f21(tests.get("f21")[11][3][0]) == tests.get("f21")[11][3][1], "error f21"
assert f21(tests.get("f21")[11][4][0]) == tests.get("f21")[11][4][1], "error f21"

assert f22(tests.get("f22")[11][0][0]) == tests.get("f22")[11][0][1], "error f22"
assert f22(tests.get("f22")[11][1][0]) == tests.get("f22")[11][1][1], "error f22"
assert f22(tests.get("f22")[11][2][0]) == tests.get("f22")[11][2][1], "error f22"
assert f22(tests.get("f22")[11][3][0]) == tests.get("f22")[11][3][1], "error f22"
assert f22(tests.get("f22")[11][4][0]) == tests.get("f22")[11][4][1], "error f22"

assert f23(tests.get("f23")[11][0][0]) == tests.get("f23")[11][0][1], "error f23"
assert f23(tests.get("f23")[11][1][0]) == tests.get("f23")[11][1][1], "error f23"
assert f23(tests.get("f23")[11][2][0]) == tests.get("f23")[11][2][1], "error f23"
assert f23(tests.get("f23")[11][3][0]) == tests.get("f23")[11][3][1], "error f23"
assert f23(tests.get("f23")[11][4][0]) == tests.get("f23")[11][4][1], "error f23"

print("pass")
