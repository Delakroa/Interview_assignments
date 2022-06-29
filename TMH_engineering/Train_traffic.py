"""Выполнение задания ТМХ"""


class TrainSchedule:
    """Создание класса расписания поездов"""

    def __init__(self):
        """Инициализация атрибут"""

    def control_point(self):
        """Установка пункта отправления"""
        while True:
            try:
                point = int(input("Введите номер пункта отправления (Один из четырёх) : "))
                if point > 4 or point <= 0:
                    print("Неверное значение пункта. Их всего четыре. \n")

                else:
                    print(f"Выбран пункт оправления {point}")
                    break
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def departure_time(self):
        """Установка времени отправления"""
        while True:
            try:
                print("Укажите время отправления поезда")

                d_time_hour, d_time_minutes = map(int, input("Введите часы и минуты через пробел: ").split())

                if d_time_hour > 24 or d_time_hour < 0:
                    print("Некорректный ввод часов.\n")

                elif d_time_minutes > 59 or d_time_minutes < 0:
                    print("Некорректный ввод минут.\n")

                else:
                    print(f"\nВремя отправления поезда {d_time_hour}ч. : {d_time_minutes}мин.\n")
                    return d_time_hour

            except ValueError:
                print("Некорректный ввод. Введите числовое значение\n")

    def arrival_time(self):
        """Установка времени прибытия"""
        while True:
            try:
                print("Установите время прибытия поезда")

                a_time_hour, a_time_minutes = map(int, input("Введите часы и минуты через пробел: ").split())

                if a_time_hour > 24 or a_time_hour < 0:
                    print("Некорректный ввод часов.\n")

                elif a_time_minutes > 59 or a_time_minutes < 0:
                    print("Некорректный ввод минут.\n")

                # Время отправленя не может быть < времени прибытия.
                elif self.departure_time() >= a_time_hour:
                    print("Неверный ввод данных. Время прибытия не может быть меньше времени!\n")

                else:
                    print(f"\nВремя прибытия поезда в {a_time_hour}ч. : {a_time_minutes}мин.\n")

                    return a_time_hour

            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def travel_time(self, distance, speed):
        """Расчёт времени в пути"""
        try:
            time = float(distance / speed)  # Время = расстояние / скорость
            if time <= 0:
                print("Неверный вариант ввода данных: Дистанция не может быть нулевым значением")

            elif distance == 1:
                print(f"Время прибытия {time * 60} минуты")

            else:
                return print(f"Расчётное время прибытие: {time} часа.")
        except ZeroDivisionError:
            print("Скорость не может быть нулевым значением!")

    # def parking_time(self):
    #     """Расчёт времени стоянки"""
    #     pass


ts = TrainSchedule()

# ts.control_point()
# ts.departure_time()
ts.arrival_time()
