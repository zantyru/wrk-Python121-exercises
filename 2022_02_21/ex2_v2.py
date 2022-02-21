class Human:
    def __init__(self, name="Аноним", age=18, height=1.7):
        self.name = str(name)
        self.age = int(age)
        self.height = float(height)


class Builder(Human):
    def __init__(self, **kwargs):
        super(Builder, self).__init__(**kwargs)
        self.preferable_tool = "Инструмент не указан"


class Sailor(Human):
    def __init__(self, **kwargs):
        super(Sailor, self).__init__(**kwargs)
        self.ship = "Корабль не указан"


class Pilot(Human):
    def __init__(self, airship_type="Неопр.", airship="Неопр.", **kwargs):
        super(Pilot, self).__init__(**kwargs)
        self.airship_type = str(airship_type)
        self.airship = str(airship)


if __name__ == '__main__':
    person1 = Human(name="Николай", age=27, height=1.74)

    person2_b = Builder()
    person2_b.preferable_tool = "Шпатель"

    person3_s = Sailor(name="Фёдор", age=56, height=1.57)
    person3_s.ship = "Стремительный"

    person4_p = Pilot(
        name="Сергей", age=23, height=1.66,
        airship_type="Вертолёт", airship="Красный"
    )

    print(isinstance(person1, Builder))  # False
    print(isinstance(person2_b, Sailor))  # False
    print(isinstance(person2_b, Human))  # True
