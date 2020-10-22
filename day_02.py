def text_analyzer(text_to_analize: str, max_length: int):
    length_of_text = len(text_to_analize)
    without_space = len(text_to_analize.split())

    # print(length_of_text, without_space)
    print("Количество символов в тексте " + str(length_of_text))
    print("Количество символов без учета пробелов " + str(without_space))
    if length_of_text < max_length:
        print('Длина текста превышает длину ' + str(max_length) + ' символов')

    if length_of_text % 2:
        print("количество символов в тексте четное")
    else:
        print("количество символов в тексте нечетное")


text_analyzer("Само собой, если на самом деле длина текста меньше максимальной, то это писать не надо.", 30)
