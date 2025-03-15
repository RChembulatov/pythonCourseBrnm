import random
import json


# Модуль 5. Уровень 1
class StringVar:
    def __init__(self, value="initial value"):
        self.value = value

    def set(self, new_value):
        self.value = new_value

    def get(self):
        return self.value


string_var = StringVar()

print(
    "Модуль 1. Уровень 1: ",
    string_var.get(),  # initial value
    string_var.set("test value"),
    string_var.get()  # test value
)


# Модуль 5. Уровень 2
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def get_coordinates(self):
        return (self.x, self.y)

    def set_coordinates(self, x, y):
        self.x = x
        self.y = y

    def calc_distance_between_two_points(self, second_x, second_y):
        return ((second_x - self.x)**2 + (second_y - self.y)**2) ** 0.5


point_init = Point()

print(
    "Модуль 5. Уровень 2: ",
    point_init.get_coordinates(),  # (0, 0)
    point_init.set_coordinates(2, 3),
    point_init.calc_distance_between_two_points(5, 7)  # 5
)


# Модуль 5. Уровень 3
class Warrior:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.armor = 100
        self.endurance = 100

    def set_health(self, health):
        self.health = health

    def defense(self):
        print(f"{self.name} Защитился. Броня: {self.armor}")

        return

    def attack(self, enemy, is_both_attack=False):
        # Если есть броня и оба воина не атакуют друг друга
        if enemy.armor > 0 and not is_both_attack:
            d_health = random.randint(0, 20)
        else:
            d_health = random.randint(10, 30)

        if self.endurance > 0:
            self.endurance -= 10
        else:
            # Если нет выносливости
            d_health = random.randint(0, 10)

        if enemy.armor > 0:
            enemy.armor -= 10

        if enemy.health > 0:
            enemy.health -= d_health

            print(f"{self.name} атаковал. Здоровье {enemy.name}: {enemy.health}")

            return enemy.health


# Установить здоровье первого воина после атаки второго
def set_warrior_one_health(warrior_one, warrior_two):
    warrior_one_health = warrior_two.attack(warrior_one)
    warrior_one.set_health(warrior_one_health)


# Установить здоровье второго воина после атаки первого
def set_warrior_two_health(warrior_one, warrior_two):
    warrior_two_health = warrior_one.attack(warrior_two)
    warrior_two.set_health(warrior_two_health)


def get_message_about_kill_warrior(name):
    is_kill = input(f"Убить {name} или нет? ").lower()

    return f"Убить {name}" if (is_kill == "да" or is_kill == "yes") else f"Пощадить {name}"


def battle(warrior_one, warrior_two):
    # Цикл до первого проигравшего
    while warrior_one.health > 0 and warrior_two.health > 0:
        is_first_warrior_attack = random.random() < 0.5
        is_second_warrior_attack = random.random() < 0.5

        # Если оба воина атакуют
        if is_first_warrior_attack and is_second_warrior_attack:
            set_warrior_one_health(warrior_one, warrior_two)
            set_warrior_two_health(warrior_one, warrior_two)
        # Если оба воина защищаются
        elif not is_first_warrior_attack and not is_second_warrior_attack:
            warrior_one.defense()
            warrior_two.defense()
        # Если только один воин атакует
        else:
            if is_first_warrior_attack:
                set_warrior_two_health(warrior_one, warrior_two)
            else:
                warrior_one.defense()

            if is_second_warrior_attack:
                set_warrior_one_health(warrior_one, warrior_two)
            else:
                warrior_two.defense()

        if warrior_one.health <= 10:
            print(warrior_two.name, "Победил!")
            print(get_message_about_kill_warrior(warrior_one.name))

            break
        elif warrior_two.health <= 10:
            print(warrior_one.name, "Победил!")
            print(get_message_about_kill_warrior(warrior_two.name))

            break


warrior_one = Warrior("Воин 1")
warrior_two = Warrior("Воин 2")

battle(warrior_one, warrior_two)


# Модуль 5. Уровень 4
class Model:
    def __init__(self, title, text, author):
        self.title = title
        self.text = text
        self.author = author

    def save(self):
        attributes = {key: value for key,
                      value in self.__dict__.items() if not key.startswith('_')}

        with open("attributes.json", "w", encoding='utf-8') as file:
            json.dump(attributes, file, ensure_ascii=False)


attributes = Model(
    title='Какой-то заголовок',
    text='Какой-то текст',
    author='Какой-то автор'
)

attributes.save()
