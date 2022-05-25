import openpyxl
import json

with open("E:/python_library/Interview_assignments/Parsing_task1/test1.json", "r", encoding="utf-8") as file1:
    data_1 = json.load(file1)

with open("E:/python_library/Interview_assignments/Parsing_task1/test2.json", "r", encoding="utf-8") as file2:
    data_2 = json.load(file2)

with open("E:/python_library/Interview_assignments/Parsing_task1/test3.json", "r", encoding="utf-8") as file3:
    data_3 = json.load(file3)


def pull_data_headers(data):
    """Парсим JSON["headers"]"""
    data_quckinfo = []
    for i in data_1["headers"]:
        for value in i.values():
            quick_info = value["QuickInfo"]
            data_quckinfo.append(quick_info)
    return data_quckinfo


def pull_data_value(data):
    """Парсим JSON["values"]"""
    data_text = []
    for i in data_1["values"]:
        for value in i.values():
            text = value["Text"]
            data_text.append(text)
    return data_text


print(pull_data_headers(data_1))
print(pull_data_value(data_1))
