"""
class Struct:
    s_size = None
    name = None
    struct = None

    def __init__(self, name, s_size):
        self.s_size = s_size
        self.name = name
        keys = ['{}{}'.format(self.name, i) for i in range(1, self.s_size + 1)]
        self.struct = dict.fromkeys(keys)

    @staticmethod
    def retype(value):
        if isinstance(value, dict) or isinstance(value, list):
            return value
        elif isinstance(value, int):
            return int(value)
        elif isinstance(value, float):
            return float(value)
        elif isinstance(value, bytes):
            return value.decode("utf-8")
        else:
            return str(value)

    def fill(self, value):
        for i in range(1, self.s_size + 1):
            self.struct['{}{}'.format(self.name, i)] = self.retype(value[i - 1])

    def build(self):
        return self.struct
"""