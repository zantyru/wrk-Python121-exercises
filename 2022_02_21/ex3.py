class Passport:
    def __init__(self,
                 number="", despense_date="",
                 patronimyc="?", name="?", surname="?",
                 birth_year=1900, birth_month=1, birth_day=1):
        self.__serial = "0000"  # Не доступно напрямую в классе ForeignPassport
        self.number = str(number)
        self.despense_date = str(despense_date)
        self.patronimyc = str(patronimyc)
        self.name = str(name)
        self.surname = str(surname)
        self.birth_year = int(birth_year)
        self.birth_month = int(birth_month)
        self.birth_day = int(birth_day)

    @property
    def serial(self):
        return self.__serial

    @serial.setter
    def serial(self, new_serial):
        if new_serial.isdigit() and len(new_serial) == 4:
            self.__serial = new_serial
        else:
            raise ValueError()


class ForeignPassport(Passport):
    def __init__(self, visas="", **kwargs):
        super(ForeignPassport, self).__init__(**kwargs)
        self.visas = str(visas)


if __name__ == '__main__':
    fp = ForeignPassport()
    print(f"{fp.serial=}")
    fp.serial = "3423"
    print(f"{fp.serial=}")
