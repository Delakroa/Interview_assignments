

class TrainSchedule:
    """Создание класса расписания поездов"""

    def point_of_departure(self):
        """Установка пункта отправления"""
        while True:
            try:
                point_departure = int(
                    input("Введите номер пункта отправления (Один из четырёх) : "))
                if point_departure > 4 or point_departure <= 0:
                    print("Неверное значение пункта. Их всего четыре. \n")

                else:
                    print(f"Выбран пункт оправления {point_departure}")
                    return point_departure
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def departure_time(self):
        """Установка времени отправления"""
        while True:
            try:
                print("Укажите время отправления поезда")

                d_time_hour, d_time_minutes = map(int, input(
                    "Введите часы и минуты через пробел: ").split())

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

                a_time_hour, a_time_minutes = map(int, input(
                    "Введите часы и минуты через пробел: ").split())

                if a_time_hour > 24 or a_time_hour < 0:
                    print("Некорректный ввод часов.\n")

                elif a_time_minutes > 59 or a_time_minutes < 0:
                    print("Некорректный ввод минут.\n")

                # Создание данной логики оставил на потом.
                # Время отправленя не может быть < времени прибытия.
                # elif self.departure_time() >= a_time_hour:
                #     print("Неверный ввод данных. Время прибытия не может быть меньше времени отправления!\n")

                else:
                    print(f"\nВремя прибытия поезда в {a_time_hour}ч. : {a_time_minutes}мин.\n")
                    return a_time_hour

            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def point_of_arrival(self):
        """Пункт прибытия"""
        # Позже нужно будет реализовать логику( пункт отправления не может быть < пункта прибытия)
        while True:
            try:
                point_arrival = int(
                    input("Введите номер пункта прибытия (Один из четырёх) : "))
                if point_arrival > 4 or point_arrival <= 0:
                    print("Неверное значение пункта. Их всего четыре. \n")

                else:
                    print(f"Выбран пункт оправления {point_arrival}")
                    return point_arrival
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def calculation_parking_time(self):
        """Расчёт времени стоянки на промежуточных станциях"""
        # Должно высчитываться автоматически.
        # parking_time = ещё не придумал
        pass

    def calculating_travel_time(self, distance, speed):
        """Расчёт времени в пути между промежуточными станциями"""
        # Должно высчитываться автоматически

        # s - расстояние (м, км)
        # v - скорость (м/сек, км/час.)
        # t -время (сек, мин, часы)
        # формула скорости v = s/t
        # формула пути s = v * t - чтобы найти расстояние, нужно умножить скорость на время движения.
        # формула времени t = s/v

        try:
            time = int(distance / speed)  # Время = расстояние / скорость
            if time <= 0:
                print("Неверный вариант ввода данных: Дистанция не может быть нулевым значением")

            elif distance == 1:
                print(f"Время прибытия {time * 60} минуты")

            else:
                return print(f"Расчётное время прибытие: {time} часов.")
        except ZeroDivisionError:
            print("Скорость не может быть нулевым значением!")


ts = TrainSchedule()

# ts.point_of_departure()
# ts.departure_time()
# ts.arrival_time()
# ts.point_of_arrival()
# ts.calculation_parking_time()
ts.calculating_travel_time(distance=1300, speed=130)
