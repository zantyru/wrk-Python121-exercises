class A:
    def __init__(self):
        self.value = 0

    def __str__(self):
        class_name = self.__class__.__name__
        return f"<class {class_name}> value = {self.value}"


class B(A):
    def __init__(self):
        super(B, self).__init__()
        self.is_enabled = True

    def __str__(self):
        s = super().__str__()
        return f"{s} is_enabled={self.is_enabled}"


if __name__ == '__main__':
    a = A()
    print(a)
    b = B()
    print(b)
