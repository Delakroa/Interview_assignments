import json
import pandas as pd


with open("E:/python_library/Interview_assignments/Parsing_task1/test1.json", "r", encoding="utf-8") as file1:
    data_1 = json.load(file1)

with open("E:/python_library/Interview_assignments/Parsing_task1/test2.json", "r", encoding="utf-8") as file2:
    data_2 = json.load(file2)

with open("E:/python_library/Interview_assignments/Parsing_task1/test3.json", "r", encoding="utf-8") as file3:
    data_3 = json.load(file3)


class Parser:
    """Создание класса парсера"""

    def __init__(self, data):
        """Инициация экземпляра класса"""
        self.data = data  # Статический атрибут

    def pull_data_headers(self):
        """Парсим JSON["headers"]"""
        data_quckinfo = []
        for i in data_1["headers"]:
            for value in i.values():
                quick_info = value["QuickInfo"]
                data_quckinfo.append(quick_info)
        return data_quckinfo

    def pull_data_value(self):
        """Парсим JSON["values"]"""
        data_text = []
        for i in data_1["values"]:
            for value in i.values():
                text = value["Text"]
                data_text.append(text)
        return data_text


ps_json1 = Parser(data_1)  # Статический метод создание класса
ps_json2 = Parser(data_2)
ps_json3 = Parser(data_3)

ps1_headers = ps_json1.pull_data_headers()
ps1_value = ps_json1.pull_data_value()

ps2_headers = ps_json2.pull_data_headers()
ps2_value = ps_json2.pull_data_value()

ps3_headers = ps_json3.pull_data_headers()
ps3_value = ps_json3.pull_data_value()

# ---------------------------------------------------------------------------------------------------------

salaries1 = pd.DataFrame([ps1_headers, ps1_value])
salaries2 = pd.DataFrame([ps2_headers, ps2_value])
salaries3 = pd.DataFrame([ps3_headers, ps3_value])

salary_sheets = {'Лист1': salaries1, 'Лист2': salaries2, 'Лист3': salaries3}
writer = pd.ExcelWriter('./salaries.xlsx', engine='xlsxwriter')

for sheet_name in salary_sheets.keys():
    salary_sheets[sheet_name].to_excel(writer, sheet_name=sheet_name, index=False)


writer.save()
