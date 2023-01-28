import random
import math

def task_1():  # Задача 1
    """   Напишите программу, которая принимает на вход цифру, 
    обозначающую день недели, и проверяет, является ли этот день выходным.
    Пример:
      - 6 -> да
      - 7 -> да
      - 1 -> нет """

    print('\n   - - - - -Задача 1 - - - - - -')
    print('      Проверяем на входе цифру ')
    print('и проверяем является введеный день недели выходным?')
    number = random.randint(1, 7)
    if number > 0 and number < 8:
        if number > 0 and number < 6:
            print(
                f" {number} -> нет, {Week(number)} это будний день. Пора на работу!")
        elif number == 6 or number == 7:
            print(f" {number} -> да, {Week(number)} это выходной день. Нужен отдых!")
    else:
        print("Ввод неверный!")

def task2():  # Задача 2
    """ Напишите программу для. проверки истинности утверждения 
    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
    """
    print('\n   - - - - -Задача 2 - - - - - -')
    print('   Проверка истинности утверждения:')
    print("    ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z \n")
    xyz11 = not (0 & 0 & 0)
    xyz12 = not (0 & 1 & 1)
    xyz13 = not (1 & 0 & 1)
    xyz14 = not (1 & 1 & 0)

    xyz21 = 1 ^ 1 ^ 1
    xyz22 = 1 ^ 0 ^ 0
    xyz23 = 0 ^ 1 ^ 0
    xyz24 = 0 ^ 0 ^ 1

    print(" 1. Выражение истинности ¬(X ⋁ Y ⋁ Z): ")  # & Коньюкция
    print("¬ (X  ⋁  Y  ⋁  Z) ")
    print(f"¬(|0| & |0| & |0|) -> {int(not(0 & 0 & 0))}")
    print(f"¬(|0| & |1| & |1|) -> {int(not(0 & 1 & 1))}")
    print(f"¬(|1| & |0| & |1|) -> {int(not(1 & 0 & 1))}")
    print(f"¬(|1| & |1| & |0|) -> {int(not(1 & 1 & 0))}")
    print()
    print(" 2. Выражение истинности ¬X ⋀ ¬Y ⋀ ¬Z: ")  # ^ Дизьюнкция
    print(" ¬X  ⋀  ¬Y  ⋀  ¬Z")
    print(f"¬|0| ^ ¬|0| ^ ¬|0| -> {1 ^ 1 ^ 1}")
    print(f"¬|0| ^ ¬|1| ^ ¬|1| -> {1 ^ 0 ^ 0}")
    print(f"¬|1| ^ ¬|0| ^ ¬|1| -> {0 ^ 1 ^ 0}")
    print(f"¬|1| ^ ¬|1| ^ ¬|0| -> {0 ^ 0 ^ 1}")
    print()
    print(" 3. Проверка истинности утверждения: ")
    print("¬ (X  ⋁  Y  ⋁  Z)  =  ¬X  ⋀  ¬Y  ⋀  ¬Z")
    print(f"¬(|0| & |0| & |0|) = ¬|0| ^ ¬|0| ^ ¬|0| -> {xyz11 == xyz21}")
    print(f"¬(|0| & |1| & |1|) = ¬|0| ^ ¬|1| ^ ¬|1| -> {xyz12 == xyz22}")
    print(f"¬(|1| & |0| & |1|) = ¬|1| ^ ¬|0| ^ ¬|1| -> {xyz13 == xyz23}")
    print(f"¬(|1| & |1| & |0|) = ¬|1| ^ ¬|1| ^ ¬|0| -> {xyz14 == xyz24}")
    print()


def task3():  # Задача 3
    """ Напишите программу, которая принимает на вход координаты точки (X и Y), 
    причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка 
    (или на какой оси она находится).
    Пример:
    - x=34; y=-30 -> 4
    - x=2; y=4-> 1
    - x=-34; y=-30 -> 3"""

    print('\n   - - - - -Задача 3 - - - - - -')
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    quater = quaters(x, y)
    if quater > 0 and quater < 5:
        print(f"Координаты точки A({x}, {y}) -> {quater} четверть.")
    elif quaters(x, y) == 5:
        print(f"Координаты точки A({x}, {y}) -> {pointsQuaters(quater)}")
    elif quaters(x, y) == 6:
        print(f"Координаты точки A({x}, {y}) -> {pointsQuaters(quater)}")
    elif quaters(x, y) == 7:
        print(f"Координаты точки A({x}, {y}) -> {pointsQuaters(quater)}")
    print()


def task4():  # Задача 4
    """ Напишите программу, которая по заданному номеру четверти, 
    показывает диапазон возможных координат точек в этой четверти (x и y).. """
    print('\n   - - - - -Задача 4 - - - - - -')
    x = random.randint(-10, 10)
    y = random.randint(-10, 10)
    quater = quaters(x, y)
    if quater > 0 and quater < 5:
        print(
            f"Диапазон возможных координат точек: {quater} четверть -> {pointsQuaters(quater)}")
    elif quaters(x, y) == 5:
        print(
            f"Диапазон возможных координат точек при x = 0 -> {pointsQuaters(quater)}")
    elif quaters(x, y) == 6:
        print(
            f"Диапазон возможных координат точек при y = 0 -> {pointsQuaters(quater)}")
    elif quaters(x, y) == 7:
        print(
            f"Диапазон возможных координат точек в центре -> {pointsQuaters(quater)}")
    print()


def task5():  # Задача 5
    """ Напишите программу, которая принимает на вход 
    координаты двух точек и находит расстояние между ними в 2D пространстве.
    Пример:
    - A (3,6); B (2,1) -> 5,09
    - A (7,-5); B (1,-1) -> 7,21"""

    print('\n   - - - - -Задача 5 - - - - - -')
    print('Программа, которая принимает на вход координаты')
    print('двух точек и находит расстояние между ними.')

    pointA = [random.randint(-10, 10), random.randint(-10, 10)]
    pointB = [random.randint(-10, 10), random.randint(-10, 10)]
    print(
        f"Кординаты точек: A({pointA[0]}, {pointA[1]}), B({pointB[0]}, {pointB[1]})")
    print(
        f"Расстояние между точками A({pointA[0]} и {pointA[1]}), B({pointB[0]}, {pointB[1]})", end=' -> ')
    print(f"{distancePoint2D(pointA, pointB)}")
    print()

    
def Week(num):
    if num == 1:
        return "Понедельник"
    if num == 2:
        return "Вторник"
    if num == 3:
        return "Среда"
    if num == 4:
        return "Четверг"
    if num == 5:
        return "Пятница"
    if num == 6:
        return "Суббота"
    if num == 7:
        return "Воскресенье"

    
def distancePoint2D(pointA, pointB):
    """ 
    Функция вычисления расстояния между двумя точками в 2D пространстве
    """
    result = (math.pow((pointB[0] - pointA[0]), 2)) + \
        (math.pow((pointB[1] - pointA[1]), 2))
    result = round(math.sqrt(result), 2)
    return result


def quaters(x, y):
    """
    Номер четверти по точке в декартовой системе координат
    :x - координата точки по  абциссс
    :y - координата точки по ординат
    :return - номер четверти  
    """
    if x > 0 and y > 0:                # 1 четверть
        return 1
    elif x < 0 and y > 0:              # 2 четверть
        return 2
    elif x < 0 and y < 0:              # 3 четверть
        return 3
    elif x > 0 and y < 0:              # 4 четверть
        return 4
    elif x == 0 and (y < 0 or y > 0):  # точка лежит на ординат
        return 5
    elif y == 0 and (x < 0 or x > 0):  # точка лежит на абцисс
        return 6
    elif x == 0 and y == 0:            # точка в центре
        return 7


def pointsQuaters(quater):
    """
    Диапазон возможных координат точек в четверти
    :quater - четверть
    :return - диапазон точек  
    """
    if quater == 1:
        return 'x > 0 и y > 0'
    elif quater == 2:
        return 'x < 0 и y > 0'
    elif quater == 3:
        return 'x < 0 и y < 0'
    elif quater == 4:
        return 'x > 0 и y < 0'
    elif quater == 5:
        return 'точка лежит на ординат, возможный диапазон точек y < 0 и y > 0'
    elif quater == 6:
        return 'точка лежит на абцисс, возможный диапазон точек x < 0 и x > 0'
    elif quater == 7:
        return 'x = 0 и y = 0'


task1() # Задача 1
task2() # Задача 2
task3() # Задача 3
task4() # Задача 4
task5() # Задача 5
