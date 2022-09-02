import sqlite3
from sqlite3 import Error


def sql_connection():
    """Подключаемся к нашей БД"""
    try:
        con = sqlite3.connect('mydatabase.db')

        return con

    except Error:
        print(Error)


def sql_table(con):
    """Создаём таблицу"""
    try:
        cursorOdj = con.cursor()

        cursorOdj.execute("CREATE TABLE timetable"
                          "(id integer PRIMARY KEY AUTOINCREMENT,"
                          " points_of_departure_and_arriva,"
                          " departure_time text,"
                          " arrival_time text,"
                          " travel_time text,"
                          " time_between_stops text)")
        con.commit()
    except sqlite3.OperationalError:
        print("Таблица уже создана!")


def sql_insert(con, entities):
    """Добавление данных в таблицу"""

    cursorObj = con.cursor()

    cursorObj.execute(
        "INSERT INTO timetable(points_of_departure_and_arriva, "
        "departure_time, arrival_time, travel_time, time_between_stops)")

    con.commit()


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
                    return self.point_departure, self.point_arrival
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def point_calculation(self):
        """Высчитываем количество промежутков между пунктами назначения"""
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
                    return self.d_time_hour, self.d_time_minutes
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
                    return self.a_time_hour, self.a_time_minutes
            except ValueError:
                print("Неверный ввод. Введите числовое значение\n")

    def time_calculation(self):
        """Расчет времени в пути"""
        self.full_time_hours = int(self.a_time_hour - self.d_time_hour)
        self.full_time_minutes = int(self.a_time_minutes - self.d_time_minutes)
        print(f"Поезд ехал: {self.full_time_hours} часа : {self.full_time_minutes} минут")
        return self.full_time_hours, self.full_time_minutes

    def calculation_parking_time(self):
        """Расчёт времени стоянки на промежуточных станциях"""
        # Должно высчитываться автоматически.
        # Parking_time = что-то
        pass

    def calculating_travel_time(self):
        """Расчёт времени в пути между промежуточными станциями"""
        # Должно высчитываться автоматически
        intermediate_hours = int(self.full_time_hours / self.final_destination)  # Часы делим на пункт назначения
        intermediate_minute = round(self.full_time_minutes / self.final_destination, 1)
        if self.final_destination <= 1:
            print(f"Промежуточные станции отсутствуют.")
        else:
            print(f"Расчётное время в пути между станциями {intermediate_hours} часа(ов) "
                  f"{intermediate_minute} минут.")
            return intermediate_hours, intermediate_minute


ts = TrainSchedule()
tspodaa = ts.point_of_departure_and_arrival()
ts.point_calculation()
tdt = ts.departure_time()
tat = ts.arrival_time()
ttc = ts.time_calculation()
# ts.calculation_parking_time()
tctt = ts.calculating_travel_time()

entities = (tspodaa, tdt, tat, ttc, tctt)
con = sql_connection()
# sql_table(con)
sql_insert(con, entities)
