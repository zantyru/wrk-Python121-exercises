class A:
    def say(self):
        return "Aaaaaa!"


class B:
    def say(self):
        return "Bebebebebe!"


class C:
    def say(self):
        return "Caution!"


if __name__ == '__main__':
        L = [A(), B(), B(), C(), A(), C(), B()]

        for obj in L:
            print(obj.say())
