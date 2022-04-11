import cloakroom as cr


def save(full_file_name, cloakroom_instance):

    free_tags = [
        # Тут распаковка
        *cloakroom_instance.get_free_tags()
    ]

    acquired_tags = [
        # Это list comprehension
        -tag
        for tag in cloakroom_instance.get_acquired_tags()
    ]

    with open(full_file_name, "w", encoding="utf-8") as f:

        # for tag in free_tags:
        #     print(tag, file=f)

        print(*free_tags, sep="\n", file=f)

        # for tag in acquired_tags:
        #     print(tag, file=f)

        print(*acquired_tags, sep="\n", file=f)


def load(full_file_name, cloakroom_instance):

    try:
        # Загружаем все строки из файла в список
        with open(full_file_name, "r", encoding="utf-8") as f:
            text_lines = f.readlines()

        # Деламем так, чтобы в гардеробе все номерки стали
        # выданными
        while True:
            try:
                _ = cloakroom_instance.acquire_free_tag()
            except cr.NotEnoughTagsError:
                break

        # Перебираем ранее загруженный список номерков
        # и возвращаем в гардероб те номерки, которые
        # должны быть свободными (они в файле были
        # положительными числами записаны)
        for text in text_lines:
            try:
                tag = int(text)
                if tag > 0:
                    try:
                        cloakroom_instance.return_tag(tag)
                    except (cr.TagAlreadyReturnedError, cr.UnknownTagError) as _:
                        pass
            except (TypeError, ValueError) as _:
                pass

    except FileNotFoundError:
        pass

