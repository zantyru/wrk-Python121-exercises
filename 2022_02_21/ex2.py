class Human:
    def __init__(self, name, age, height):
        self.name = str(name)
        self.age = int(age)
        self.height = float(height)


class Builder(Human):
    def __init__(self, name, age, height):
        super(Builder, self).__init__(name, age, height)
        self.preferable_tool = "Инструмент не указан"


class Sailor(Human):
    def __init__(self, name, age, height):
        super(Sailor, self).__init__(name, age, height)
        self.ship = "Корабль не указан"


class Pilot(Human):
    def __init__(self, name, age, height, airship_type, airship):
        super(Pilot, self).__init__(name, age, height)
        self.airship_type = str(airship_type)
        self.airship = str(airship)


if __name__ == '__main__':
    person1 = Human("Николай", 27, 1.74)

    person2_b = Builder("Майкл", 45, 1.89)
    person2_b.preferable_tool = "Шпатель"

    person3_s = Sailor("Фёдор", 56, 1.57)
    person3_s.ship = "Стремительный"

    person4_p = Pilot("Сергей", 23, 1.66, "Вертолёт", "Красный")

    print(isinstance(person1, Builder))  # False
    print(isinstance(person2_b, Sailor))  # False
    print(isinstance(person2_b, Human))  # True
