"""Фаил содержит переменные и ссылки для тестов"""


class Link():
    """Класс для ссылок"""

    def __init__(self, driver_chrome, fns_russia) -> None:
        """Инициализация атрибута класса"""
        self.driver_chrome = driver_chrome
        self.fns_russia = fns_russia

    def driver_path(self):
        """Дирректория драйвера"""
        self.driver_chrome = r'D:/Python library/Interview_assignments/CKR_company/REST_task2/hromedriver.exe'
        return self.driver_chrome

    def get_site(self):
        """Сайт с которым работаем"""
        self.fns_russia = 'https://service.nalog.ru/addrno.do'
