class Base:

    def do(self):
        return f"Do: {self.say()}"

    def say(self):
        return "----"


class A(Base):
    def __init__(self):
        super(A, self).__init__()

    # def say(self):
    #     return "Aaaaaa!"


class B(Base):
    def __init__(self):
        super(B, self).__init__()

    def say(self):
        return "Bebebebebe!"


class C(Base):
    def __init__(self):
        super(C, self).__init__()

    def say(self):
        return "Caution!"


if __name__ == '__main__':
        L = [A(), B(), B(), C(), A(), C(), B()]

        for obj in L:
            print(obj.say())

        print()

        for obj in L:
            print(obj.do())
