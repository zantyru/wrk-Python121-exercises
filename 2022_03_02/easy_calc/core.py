ERROR_TEXT = "Ошибка!"


def get_number_or_none(text_value):
    try:
        x = float(text_value)
    except ValueError:
        x = None
    except TypeError:
        x = None

    return x


def do_addition(left, right):
    left = get_number_or_none(left)
    right = get_number_or_none(right)

    if left is not None and right is not None:
        result = left + right
    else:
        result = ERROR_TEXT

    return result


def do_subtraction(left, right):
    left = get_number_or_none(left)
    right = get_number_or_none(right)

    if left is not None and right is not None:
        result = left - right
    else:
        result = ERROR_TEXT

    return result


def do_multiplication(left, right):
    left = get_number_or_none(left)
    right = get_number_or_none(right)

    if left is not None and right is not None:
        result = left * right
    else:
        result = ERROR_TEXT

    return result


def do_division(left, right):
    left = get_number_or_none(left)
    right = get_number_or_none(right)

    if left is not None and right is not None:
        try:
            result = left / right
        except ZeroDivisionError:
            result = ERROR_TEXT
    else:
        result = ERROR_TEXT

    return result
