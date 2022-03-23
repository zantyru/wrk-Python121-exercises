def save(filename, number):
    try:
        with open(filename, "a", encoding="UTF-8") as f:
            f.write(str(number))
            f.write("\n")
            # print(number, file=f)
    except IOError as e:
        print(e)


def load(filename):
    list_of_integers = []

    try:
        with open(filename, "r", encoding="UTF-8") as f:
            for line in f.readlines():
                try:
                    number = int(line)
                    list_of_integers.append(number)
                except (ValueError, TypeError) as _:
                    pass
    except FileNotFoundError as e:
        print(e)
    except IOError as e:
        print(e)

    return list_of_integers


if __name__ == "__main__":
    numbers = load("n.txt")
    print(numbers)

    save("n.txt", 10)
    save("n.txt", -7)
    save("n.txt", 9)

    numbers = load("n.txt")
    print(numbers)