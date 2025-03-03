# Модуль 1. Часть 1. Уровень 1
value = (5 + 7 * 5 / 8) / 3**5

print("Ответ по Модуль 1. Часть 1. Уровень 1: ", value)


# Модуль 1. Часть 1. Уровень 2
roadLength = 109
speed = int(input("Введите скорость: "))
time = int(input("Введите время: "))

countOfCircles = int(speed * time / roadLength)
print(
    "Ответ по Модуль 1. Часть 1. Уровень 2: ",
    abs(countOfCircles * roadLength - speed * time),
)


# Модуль 1. Часть 1. Уровень 3
firstNumber = float(input("Введите число 1: "))
secondNumber = float(input("Введите число 2: "))
maxValue = (firstNumber > secondNumber) * firstNumber + (
    secondNumber > firstNumber
) * secondNumber

print("Ответ по Модуль 1. Часть 1. Уровень 3: ", maxValue)


# Модуль 1. Часть 2. Уровень 1
firstInt = int(input("Введите целое число 1: "))
secondInt = int(input("Введите целое число 2: "))
thirdInt = int(input("Введите целое число 3: "))
if firstInt == secondInt and firstInt == thirdInt:
    print("Модуль 1. Часть 2. Уровень 1: ", 3)
elif firstInt == secondInt or firstInt == thirdInt or secondInt == thirdInt:
    print("Модуль 1. Часть 2. Уровень 1: ", 2)
else:
    print("Модуль 1. Часть 2. Уровень 1: ", 0)


# Модуль 1. Часть 2. Уровень 2
firstColChessInt = int(input("Введите целое число от 1 до 8: "))
firstRowChessInt = int(input("Введите целое число от 1 до 8: "))

secondColChessInt = int(input("Введите целое число от 1 до 8: "))
secondRowChessInt = int(input("Введите целое число от 1 до 8: "))

isValidChessInt = (
    (firstColChessInt >= 1)
    and (firstColChessInt <= 8)
    and (secondColChessInt >= 1)
    and (secondColChessInt <= 8)
    and (firstRowChessInt >= 1)
    and (firstRowChessInt <= 8)
    and (secondRowChessInt >= 1)
    and (secondRowChessInt <= 8)
)

if isValidChessInt:
    if (firstColChessInt == secondColChessInt) and (
        firstRowChessInt == secondRowChessInt
    ):
        print("Сделайте ход")
    elif (firstColChessInt == secondColChessInt) or (
        firstRowChessInt == secondRowChessInt
    ):
        print("Модуль 1. Часть 2. Уровень 2: ", "YES")
    else:
        print("Модуль 1. Часть 2. Уровень 2: ", "NO")
else:
    print("Неправильные числа")


# Модуль 1. Часть 2. Уровень 3

isValidPassword = False


def checkPassword():
    password = input("Введите пароль: ")
    i = 0
    hasLower = False
    hasUpper = False

    while i < len(password):
        if hasUpper == False:
            hasUpper = password[i].isupper()

        if hasLower == False:
            hasLower = password[i].islower()
        i += 1
    return hasUpper and hasLower and (len(password) > 8)


while isValidPassword == False:
    isValidPassword = checkPassword()

if isValidPassword:
    print("Пароль прошел валидацию")
