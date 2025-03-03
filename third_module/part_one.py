# Модуль 3. Часть 1. Уровень 1

deposit = int(input("Введите x: "))
percent = int(input("Введите p: "))
possible_deposit = int(input("Введите y: "))

year_count = 0

while deposit < possible_deposit:
    deposit += int(percent * deposit / 100)
    year_count += 1

print("Модуль 3. Часть 1. Уровень 1: ", year_count)


# Модуль 3. Часть 1. Уровень 2

count = 0
iterations = int(input("Введите число повторений : "))

while count < iterations:
    print("for - частный случай цикла while")
    count += 1


# Модуль 3. Часть 1. Уровень 3
input_value = input("Введите число: ")
total_value = 0

for elem in list(input_value):
    total_value += int(elem)

print("Сумма цифр: ", total_value)
