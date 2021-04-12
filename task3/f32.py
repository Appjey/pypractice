class C32:
    state = []

    def __init__(self):
        self.state = [None]

    def get(self):
        if self.state[-1] is None:
            self.state[-1] = 0
            return 0
        elif self.state[-1] == 0:
            self.state.append(2)
            return 2
        elif self.state[-1] == 1:
            self.state.append(3)
            return 3
        elif self.state[-1] == 2:
            self.state.append(8)
            return 8
        elif self.state[-1] == 3:
            self.state.append(5)
            return 5
        elif self.state[-1] == 4:
            self.state.append(3)
            return 3
        elif self.state[-1] == 5:
            try:
                pass
            except RuntimeError:
                pass
        elif self.state[-1] == 6:
            self.state.append(8)
            return 8
        elif self.state[-1] == 7:
            self.state.append(5)
            return 5
        elif self.state[-1] == 8:
            self.state.append(8)
            return 8

    def amble(self):
        if self.state[-1] == 0:
            self.state.append(1)
            return 1
        elif self.state[-1] == 1:
            self.state.append(4)
            return 4
        elif self.state[-1] == 2:
            self.state.append(7)
            return 7
        elif self.state[-1] == 3:
            try:
                pass
            except RuntimeError:
                pass
        elif self.state[-1] == 4:
            self.state.append(4)
            return 4
        elif self.state[-1] == 5:
            self.state.append(6)
            return 6
        elif self.state[-1] == 6:
            self.state.append(7)
            return 7
        elif self.state[-1] == 7:
            try:
                pass
            except RuntimeError:
                pass
        elif self.state[-1] == 8:
            self.state.append(7)
            return 7
