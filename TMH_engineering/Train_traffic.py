# import datetime


# Задача: написать программу «Расписание поездов».
# Данные для маршрута, следующие:
# - пункт отправления;
# - время отправления;
# - время прибытия;
# - пункт прибытия;

# Время в пути и время стоянки должны высчитываться автоматически и не должны вводиться пользователем
# (при этом пользователю они должны быть видны)
# - время стоянки на промежуточных станциях;
# - время пути между промежуточными станциями

# Функция, которая должна быть реализована:
#  - создание нового маршрута;
# - сохранение маршрута;
# Открытие и редактирование раннее созданных маршрутов (также и после перезапуска программы), следует учесть,
# что маршрут может состоять более чем из двух пунктов.
# Реализация с помощью СУБД опциональна.


class TrainSchedule:
    """Создание класса расписания поездов"""

    def __init__(self, distance, speed, point):
        self.distance = distance
        self.speed = speed
        self.point = point
        pass


def control_point():
    """Установка пункта отправления"""
    try:
        point = int(input("Введите номер пункта отправления (Один из четырёх) "))
        if point > 4 or point <= 0:
            return print("Неверное значение пункта. Их всего четыре. ")
        return print(f"Выбран пункт оправления {point}")

    except ValueError:
        print("Неверный ввод. Введите числовое значение")


def departure_time():
    """Установка времени отправления"""
    try:
        print("Укажите время отправления поезда")

        while True:
            d_time_hour = int(input("Введите часы: "))

            if d_time_hour > 24 or d_time_hour <= 0:
                print("Неверный ввод часов.")
                return int(input("Введите часы: "))

            else:
                d_time_minutes = int(input("Введите минуты: "))

                if d_time_minutes > 59 or d_time_minutes <= 0:
                    print("Неверный ввод минут.")
                    return int(input("Введите минуты: "))

            return print(f"Время отправления {d_time_hour}:{d_time_minutes}")

    except ValueError:
        print("Неверный ввод. Введите числовое значение")


def arrival_time(d_time):
    """Установка времени прибытия"""
    try:
        a_time = int(input("Установите время прибытия поезда в формате: "))
        if a_time <= d_time:
            print("Неверный ввод данных. Время прибытия не может быть меньше времени отправления")
        else:
            return print(f"Указанное время прибытия {a_time}")

    except ValueError:
        print("Неверный ввод. Введите числовое значение")


def travel_time(distance, speed):
    """Расчёт времени в пути"""
    try:
        time = float(distance / speed)  # Время = расстояние / скорость
        if time <= 0:
            return print("Неверный вариант ввода данных: Дистанция не может быть нулевым значением")

        elif distance == 1:
            return print(f"Время прибытия {time * 60} минуты")

        else:
            return print(f"Расчётное время прибытие: {time} часа.")
    except ZeroDivisionError:
        return print(f"Скорость не может быть нулевым значением!")


def parking_time():
    """Расчёт времени стоянки"""
    pass


# control_point()
departure_time()
# travel_time(1, 0)
# arrival_time(5)
