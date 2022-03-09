class NotEnoughTagsError(Exception):
    pass


class TagAlreadyReturnedError(Exception):
    pass


class UnknownTagError(Exception):
    pass


class Cloakroom:

    def __init__(self, tags_count):
        self.__tags = [*range(1, int(tags_count)+1)]
        self.__tags_acquired = []

    def acquire_free_tag(self):
        """"""
        """Возвращает свободный номерок."""
        try:
            n = self.__tags.pop()
        except IndexError:
            raise NotEnoughTagsError(
                "Нет свободных номерков."
            )
        self.__tags_acquired.append(n)
        return n

    def return_tag(self, tag):
        """"""
        """Ничего не возвращает, но принимает номерок """
        """и делает его снова доступным для повторного """
        """использования."""
        if tag not in self.__tags and tag not in self.__tags_acquired:
            raise UnknownTagError(
                f"Неизвестный номерок {tag}."
            )

        try:
            self.__tags_acquired.remove(tag)
        except ValueError:
            raise TagAlreadyReturnedError(
                f"Этот номерок уже сдан: {tag}."
            )
        self.__tags.append(tag)

    def is_tag_acquired(self, tag):
        """"""
        """Возвращает булевый тип. Показывает, выдан ли """
        """кому-либо номерок или нет."""
        if tag not in self.__tags and tag not in self.__tags_acquired:
            raise UnknownTagError(
                f"Неизвестный номерок {tag}."
            )
        return tag in self.__tags_acquired

    def get_free_tags(self):
        """"""
        """Возвращает список (а лучше - итератор) """
        """свободных номерков."""
        return iter(self.__tags)

    def get_acquired_tags(self):
        """"""
        """Возвращает список (а лучше - итератор) """
        """выданных номерков."""
        return iter(self.__tags_acquired)
