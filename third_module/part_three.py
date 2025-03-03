import re


# Модуль 3. Часть 3. Уровень 1
def area(a, b, c):
    p = (a + b + c) / 2

    return (p * (p - a) * (p - b) * (p - c)) ** 0.5


print("Модуль 3. Часть 3. Уровень 1: ", area(3, 4, 5))


# Модуль 3. Часть 3. Уровень 2
string = """Было просто пасмурно, дуло с севера
А к обеду насчитал сто градаций серого.
Так всегда первого ноль девятого
То ли весь мир сошел с ума, то ли я - того..."""


def get_words_less_five_sign(str):
    new_list = []
    str_without_line_break = str.replace("\n", " ")
    formatted_str = re.sub(r"[^a-zA-Zа-яА-Я\s]", "", str_without_line_break)

    for item in formatted_str.split(" "):
        if item and len(item) < 5:
            new_list.append(item)

    return new_list


# ['Было', 'дуло', 'с', 'А', 'к', 'сто', 'Так', 'ноль', 'То', 'ли', 'весь', 'мир', 'с', 'ума', 'то', 'ли', 'я', 'того']
print("Модуль 3. Часть 3. Уровень 2: ", get_words_less_five_sign(string))


# Модуль 3. Часть 3. Уровень 3


def get_max_value(numbers_list):
    string_list = []

    for value in numbers_list:
        value_to_string = str(value)
        string_list.append(value_to_string)

    string_list.sort(reverse=True)

    return "".join(string_list)


print("Модуль 3. Часть 3. Уровень 3", get_max_value([56, 9, 11, 2]))
print("Модуль 3. Часть 3. Уровень 3", get_max_value([3, 81, 5]))
