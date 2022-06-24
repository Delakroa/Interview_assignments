"""Выполнение задания ТМХ"""

class TrainSchedule:
    """Создание класса расписания поездов"""

    def __init__(self):
        "Инициализация атрибутов класса"
        # Установка пункта отправления
        # self.point = int(input("Введите номер пункта отправления (Один из четырёх) : "))
        # Установка времени отправления
        # self.d_time_hour = int(input("Введите часы: "))
        # self.d_time_minutes = int(input("Введите минуты: "))
        # Установка времени брибытия
        

    def control_point(self):
        """Установка пункта отправления"""
        while True:
            try:
                point = int(input("Введите номер пункта отправления (Один из четырёх) : "))
                if point > 4 or point <= 0:
                    print("Неверное значение пункта. Их всего четыре. \n")

                else:
                    print(f"Выбран пункт оправления {point}\n")
                    break

            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")


    def departure_time(self):
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
                        return  d_time_hour

            except ValueError:
                print("Некорректный ввод. Введите числовое значение\n")


    def arrival_time(self):
        """Установка времени прибытия"""
        while True:
            try:
                print("Установите время прибытия поезда")

                a_time_hour = int(input("Установите часы: "))
                if a_time_hour > 24 or a_time_hour <= 0:
                    print("Некорректный ввод часов.\n")

                else:
                    a_time_minutes = int(input("Установите минуты: "))
                    if a_time_minutes > 59 or a_time_minutes <= 0:
                        print("Некорректный ввод минут.\n")

                    else:
                        print(f"\nВремя прибытия поезда в {a_time_hour}ч. : {a_time_minutes}мин.\n")
                        # Время отправленя не может быть < времени прибытия.
                        if self.departure_time() <= a_time_hour:
                            print("Неверный ввод данных. Время прибытия не может быть меньше времени отправления!\n")

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
