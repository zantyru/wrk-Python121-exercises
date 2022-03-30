"""
Модуль реализует механизмы записи/дозаписи одного числа за раз в файл и чтения всех чисел из файла в виде списка.
"""

def save(filename, number):
    try:
        with open(filename, "a", encoding="UTF-8") as f:
            f.write(str(number))
            f.write("\n")
            # print(number, file=f)
    except IOError as e:
        # Ошибку печатаем в терминал
        print(e)


def load(filename):
    # В этом списке будет накапливаться результат
    list_of_integers = []

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            # Построчно перебираем файл
            for line in f.readlines():
                try:
                    # Пробуем получить целое число из текста
                    number = int(line)
                    list_of_integers.append(number)
                except (ValueError, TypeError) as _:
                    # Всё, что не является записью целого числа, игнорируем
                    pass
    except (FileNotFoundError, IOError) as e:
        # Ошибку печатаем в терминал
        print(e)

    return list_of_integers


# Код, который тестирует функции. Срабатывае только при прямом запуске этого файла
if __name__ == "__main__":
    numbers = load("n.txt")
    print(numbers)

    save("n.txt", 10)
    save("n.txt", -7)
    save("n.txt", 9)

    numbers = load("n.txt")
    print(numbers)