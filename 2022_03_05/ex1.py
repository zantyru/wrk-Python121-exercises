class Base:
    ...


class Derived(Base):
    ...


if __name__ == '__main__':
    var1 = Base()
    var2 = Derived()
    print(isinstance(var1, Base))  # True
    print(isinstance(var2, Base))  # True
    print(isinstance(var1, Derived))  # False
    print(isinstance(var2, Derived))  # True



