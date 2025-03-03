from random import randint

# Модуль 3. Часть 2. Уровень 1

random_list = [1, 4, 1, 6, "hello", "a", 5, "hello"]
count_of_random_value = {}
new_list = []

count = 0
for item in random_list:
    if item in count_of_random_value:
        count_of_random_value[item] += 1
    else:
        count_of_random_value[item] = 1

for value, count in count_of_random_value.items():
    if count > 1:
        new_list.append(value)

print("Модуль 3. Часть 2. Уровень 1: ", new_list)


# Модуль 3. Часть 2. Уровень 2
n = 5
matrix = [[randint(0, 100) for i in range(n)] for j in range(n)]
new_matrix = []
for arr in matrix:
    new_matrix.append(max(arr))

print(
    "Модуль 3. Часть 2. Уровень 2: ",
    max(new_matrix),
    " в матрице: ",
    matrix,
)

# Модуль 3. Часть 2. Уровень 3
dictionary = {"name1": "id1", "name2": "id2", "name3": "id3"}
reversed_dictionary = {}

for key, value in dictionary.items():
    reversed_dictionary[value] = key

print("Модуль 3. Часть 2. Уровень 3: ", reversed_dictionary)
