"""Выполнение задания ТМХ"""

# class TrainSchedule:
#     """Создание класса расписания поездов"""

#     def __init__(self, distance, speed, point):
#         self.distance = distance
#         self.speed = speed
#         self.point = point
#         pass


def control_point():
    """Установка пункта отправления"""
    while True:
        try:
            point = int(
                input("Введите номер пункта отправления (Один из четырёх) : "))
            if point > 4 or point <= 0:
                print("Неверное значение пункта. Их всего четыре. \n")

            else:
                print(f"Выбран пункт оправления {point}")
                break

        except ValueError:
            print("Неверный ввод. Введите числовое значение\n")


def departure_time():
    "Установка времени отправления"
    while True:
        try:
            print("Укажите время отправления поезда")

            d_time_hour = int(input("Введите часы: "))
            if d_time_hour > 24 or d_time_hour <= 0:
                print("Некорректный ввод часов.\n")

            else:
                d_time_minutes = int(input("Введите минуты: "))
                if d_time_minutes > 59 or d_time_minutes <= 0:
                    print("Некорректный ввод минут.\n")

                else:
                    print(f"\nВремя отправления поезда {d_time_hour}ч. : {d_time_minutes}мин.\n")
                    return d_time_hour

        except ValueError:
            print("Некорректный ввод. Введите числовое значение\n")


def arrival_time():
    """Установка времени прибытия"""
    while True:
        try:
            a_time = int(input("Установите время прибытия поезда в формате: "))
            if a_time <= departure_time():
                print(
                    "Неверный ввод данных. Время прибытия не может быть меньше времени отправления")
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
        return print("Скорость не может быть нулевым значением!")


# def parking_time():
#     """Расчёт времени стоянки"""
#     pass


# control_point()
departure_time()
# arrival_time()
# travel_time(1, 0)
