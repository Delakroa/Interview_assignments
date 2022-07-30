class TrainSchedule:
    """Создание класса графика"""

    def __init__(self):
        self.d_time_hour = None
        self.d_time_minutes = None
        self.a_time_hour = None
        self.a_time_minutes = None

    @staticmethod
    def point_of_departure_and_arrival():
        """Установка пункта отправления и пункта прибытия"""
        while True:
            try:
                point_departure, point_arrival = map(int, input(
                    "Введите номер пункта отправления и прибытия через пробел (от 1 до 4) : ").split())
                if point_departure > 4 or point_departure <= 0:
                    print("Неверное значение пункта отправления. \n")
                elif point_arrival > 4 or point_arrival <= 0:
                    print("Неверное значение пункта пункта прибытия. \n")
                elif point_arrival <= point_departure:
                    print("Время отправления, не может быть меньше или равный времени прибытия! \n")
                else:
                    print(f"Установлен пункт оправления {point_departure}, прибытие {point_arrival}\n")
                    return point_departure
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def departure_time(self):
        """Установка времени отправления"""
        while True:
            try:
                print("Укажите время отправления поезда")
                self.d_time_hour, self.d_time_minutes = map(int, input("Введите часы и минуты через пробел: ").split())
                if self.d_time_hour > 24 or self.d_time_hour < 0:
                    print("Некорректный ввод часов.\n")
                elif self.d_time_minutes > 59 or self.d_time_minutes < 0:
                    print("Некорректный ввод минут.\n")
                else:
                    print(f"\nВремя отправления поезда {self.d_time_hour}ч. : {self.d_time_minutes}мин.\n")
                    return self.d_time_hour
            except ValueError:
                print("Некорректный ввод. Введите числовое значение\n")

    def arrival_time(self):
        """Установка времени прибытия"""
        while True:
            try:
                print("Установите время прибытия поезда")
                self.a_time_hour, self.a_time_minutes = map(int, input("Введите часы и минуты через пробел: ").split())
                if self.a_time_hour > 24 or self.a_time_hour < 0:
                    print("Некорректный ввод часов.\n")
                elif self.a_time_minutes > 59 or self.a_time_minutes < 0:
                    print("Некорректный ввод минут.\n")
                elif self.d_time_hour >= self.a_time_hour:
                    print("Неверный ввод данных. Время прибытия не может быть меньше или равным времени отправления!\n")
                else:
                    print(f"\nВремя прибытия поезда в {self.a_time_hour}ч. : {self.a_time_minutes}мин.\n")
                    return self.a_time_hour
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def time_calculation(self):
        """Расчет времени в пути"""
        full_times = []  # Общение время
        full_time_hours = self.a_time_hour - self.d_time_hour
        full_times.append(full_time_hours)
        full_time_minutes = self.a_time_minutes - self.d_time_minutes
        full_times.append(full_time_minutes)
        # print(type(full_times))
        # print(full_times)
        print(f"Поезд ехал {full_time_hours} часа : {full_time_minutes} минут")

    def calculation_parking_time(self):
        """Расчёт времени стоянки на промежуточных станциях"""
        # Должно высчитываться автоматически.
        # parking_time = что-то
        pass

    @staticmethod
    def calculating_travel_time(distance, speed):
        """Расчёт времени в пути между промежуточными станциями
        Должно высчитываться автоматически

        s - расстояние (м, км)
        v - скорость (м/сек, км/час.)
        t -время (сек, мин, часы)
        формула скорости v = s/t
        формула пути s = v * t - чтобы найти расстояние, нужно умножить скорость на время движения.
        формула времени t = s/v"""

        try:
            time = int(distance / speed)  # Время = расстояние / скорость
            if time <= 0:
                print("Неверный вариант ввода данных: Дистанция не может быть нулевым значением")

            elif distance == 1:
                print(f"Время прибытия {time * 60} минуты")

            else:
                print(f"Расчётное время прибытие: {time} часов.")
                return time

        except ZeroDivisionError:
            print("Скорость не может быть нулевым значением!")


ts = TrainSchedule()

# ts.point_of_departure_and_arrival()
ts.departure_time()
ts.arrival_time()
ts.time_calculation()
# ts.calculation_parking_time()
# ts.calculating_travel_time(distance=1300, speed=130)
