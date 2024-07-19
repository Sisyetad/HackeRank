class Kangaroo:
    def __init__(self, x1, v1, x2, v2):
        self.x1 = x1
        self.v1 = v1
        self.x2 = x2
        self.v2 = v2

    def kangaroo(self):
        if self.v1 > self.v2:
            if (self.x1 - self.x2) % (self.v2 - self.v1) == 0:
                return "YES"
            else:
                return "NO"
        else:
            return "NO"