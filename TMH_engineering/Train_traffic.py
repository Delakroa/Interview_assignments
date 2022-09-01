class TrainSchedule:
    """Создание класса графика"""

    def __init__(self):
        """Инициализация атрибутов класса"""
        self.point_departure = None
        self.point_arrival = None
        self.final_destination = None
        self.d_time_hour = None
        self.d_time_minutes = None
        self.a_time_hour = None
        self.a_time_minutes = None
        self.full_time_hours = None
        self.full_time_minutes = None

    def point_of_departure_and_arrival(self):
        """Установка пункта отправления и пункта прибытия"""
        while True:
            try:
                self.point_departure, self.point_arrival = map(int, input(
                    "Введите номер пункта отправления и прибытия через пробел (от 1 до 4) : ").split())
                if self.point_departure > 4 or self.point_departure <= 0:
                    print("Неверное значение пункта отправления. \n")
                elif self.point_arrival > 4 or self.point_arrival <= 0:
                    print("Неверное значение пункта прибытия. \n")
                elif self.point_arrival <= self.point_departure:
                    print("Время отправления, не может быть меньше или равный времени прибытия! \n")
                else:
                    print(f"Установлен пункт оправления {self.point_departure}, прибытие {self.point_arrival}\n")
                    return self.point_departure
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def point_calculation(self):
        """Расчёт пункта назначения"""
        self.final_destination = int(self.point_arrival - self.point_departure)
        return self.final_destination

    def departure_time(self):
        """Установка времени отправления"""
        while True:
            try:
                print("Укажите время отправления поезда. (Формат 24 часа.)")
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
                print("Установите время прибытия поезда. (Формат 24 часа.)")
                self.a_time_hour, self.a_time_minutes = map(int, input("Введите часы и минуты через пробел: ").split())
                if self.a_time_hour > 24 or self.a_time_hour < 0:
                    print("Некорректный ввод часов.\n")
                elif self.a_time_minutes > 59 or self.a_time_minutes < 0:
                    print("Некорректный ввод минут.\n")
                elif self.d_time_hour > self.a_time_hour:
                    print("Неверный ввод данных. Время прибытия не может быть меньше или равным времени отправления!\n")
                else:
                    print(f"\nВремя прибытия поезда в {self.a_time_hour}ч. : {self.a_time_minutes}мин.\n")
                    return self.a_time_hour
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def time_calculation(self):
        """Расчет времени в пути"""
        self.full_time_hours = int(self.a_time_hour - self.d_time_hour)
        self.full_time_minutes = int(self.a_time_minutes - self.d_time_minutes)
        print(f"Поезд ехал {self.full_time_hours} часа : {self.full_time_minutes} минут")
        return self.full_time_hours

    def calculation_parking_time(self):
        """Расчёт времени стоянки на промежуточных станциях"""
        # Должно высчитываться автоматически.
        # Parking_time = что-то
        pass

    def calculating_travel_time(self):
        """Расчёт времени в пути между промежуточными станциями"""
        # Должно высчитываться автоматически
        intermediate_hours = int(self.full_time_hours / self.final_destination)  # Часы делим на пункт назначения
        intermediate_minute = float(self.full_time_minutes / self.final_destination) * 60
        if self.final_destination <= 1:
            print(f"Промежуточные станции отсутствуют.")
        else:
            print(f"Расчётное время в пути между станциями {intermediate_hours} часа(ов) "
                  f"{int(intermediate_minute)} минут.")


ts = TrainSchedule()

ts.point_of_departure_and_arrival()
ts.point_calculation()
ts.departure_time()
ts.arrival_time()
ts.time_calculation()
ts.calculation_parking_time()
ts.calculating_travel_time()
