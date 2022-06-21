import json
import pandas as pd

with open("z:/Л И Ч К А/Халиков Д. Г/Python_ТЗ/test1.json", "r", encoding="utf-8") as file1_json:
    data_1 = json.load(file1_json)

with open("z:/Л И Ч К А/Халиков Д. Г/Python_ТЗ/test2.json", "r", encoding="utf-8") as file2_json:
    data_2 = json.load(file2_json)

with open("z:/Л И Ч К А/Халиков Д. Г/Python_ТЗ/test3.json", "r", encoding="utf-8") as file3_json:
    data_3 = json.load(file3_json)


class Parser:
    """Создание класса парсера"""

    def __init__(self, data):
        """Инциализация экземпляра класса"""
        self.data = data  # Статический атрибут

    def pull_data_headers(self):
        """Парсим JSON["headers"]"""
        data_quickinfo = []
        for i in self.data["headers"]:
            for value in i.values():
                quick_info = value['QuickInfo']
                data_quickinfo.append(quick_info)
        return data_quickinfo

    def pull_data_value(self):
        """Парсим JSON["values"]"""
        data_text = []
        for i in self.data["values"]:
            for value in i.values():
                text = value['Text']
                data_text.append(text)
        return data_text


ps_data_1 = Parser(data_1)  # Статический метод создание класса
ps_data_2 = Parser(data_2)
ps_data_3 = Parser(data_3)


# --------------------------------------------------------------------------------------------------------------

def creation_sheets():
    """Создание Workbook с тремя worksheet"""
    # Обьединение списков в словарь
    zipped_value1 = dict(zip(ps_data_1.pull_data_headers(),
                             ps_data_1.pull_data_value()))
    zipped_value2 = dict(zip(ps_data_2.pull_data_headers(),
                             ps_data_2.pull_data_value()))
    zipped_value3 = dict(zip(ps_data_3.pull_data_headers(),
                             ps_data_3.pull_data_value()))

    # Создание DataFrame
    salaries1 = pd.DataFrame([zipped_value1])
    salaries2 = pd.DataFrame([zipped_value2])
    salaries3 = pd.DataFrame([zipped_value3])

    # Создание worksheet
    salary_sheets = {'Лист1': salaries1,
                     'Лист2': salaries2, 'Лист3': salaries3}
    writer = pd.ExcelWriter('./salaries.xlsx', engine='xlsxwriter')

    for sheet_name in salary_sheets.keys():
        salary_sheets[sheet_name].to_excel(
            writer, sheet_name=sheet_name, index=False)
    return writer


creation_sheets().save()
