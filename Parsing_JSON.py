import openpyxl
import json

with open('test1.json', encoding='utf-8') as file:
    data = json.load(file)
for header in data['headers']:
    text = header['properties']
    QuickInfo = text['QuickInfo']

    # print(type(QuickInfo))
    print(QuickInfo)

# Создаём рабочую книгу
book = openpyxl.Workbook()
# По умолчанию создаётся с таблицей Sheet
# print(book.sheetnames)
book.remove(book.active)

# Позиционирование на конкретном листе
# в который мы осуществляем запись
sheet_2 = book.create_sheet('Лист2')  # по умолчанию это первый лист
sheet_1 = book.create_sheet('Лист1')
sheet_3 = book.create_sheet('Лист3')

# Обращение к координатам ячейки
sheet_1['A1'] = QuickInfo[:]
sheet_1['B1'] = QuickInfo
sheet_1['C1'] = QuickInfo
sheet_1['D1'] = QuickInfo
sheet_1['E1'] = QuickInfo
sheet_1['F1'] = QuickInfo
sheet_1['G1'] = QuickInfo
sheet_1['H1'] = QuickInfo

row = 2
for header in data['headers']:
    text = header['properties']
    # Обращение по координатам [ряд][колонка]
    sheet_1[row][0].value = text['Id']
    sheet_1[row][1].value = text['Name']
    sheet_1[row][2].value = text['Sid']
    sheet_1[row][3].value = text['Enabled']
    sheet_1[row][4].value = text['X']
    sheet_1[row][5].value = text['Y']
    sheet_1[row][6].value = text['Width']
    sheet_1[row][7].value = text['Height']
    row += 1


# Чтобы изменения вступили в силу
# сохраняем книгу
book.save("my_book.xlsx")
book.close()
