import openpyxl
import json

with open('test1.json', encoding='utf-8') as file:
    data = json.load(file)
row = []
for header in data['headers']:
    text = header['properties']
    QuickInfo = text['QuickInfo']
    row.append(QuickInfo)
    # print(type(row))


# Создаём рабочую книгу
book = openpyxl.Workbook()
# По умолчанию создаётся с таблицей Sheet
# print(book.sheetnames)
book.remove(book.active)

# Позиционирование на конкретном листе
# в который мы осуществляем запись
sheet_1 = book.create_sheet('Лист1')  # по умолчанию это первый лист
sheet_2 = book.create_sheet('Лист2')
sheet_3 = book.create_sheet('Лист3')

# Обращение к координатам ячейки
sheet_1['A1'] = str(row[0:1])
sheet_1['B1'] = str(row[1:2])
sheet_1['C1'] = str(row[2:3])
sheet_1['D1'] = str(row[3:4])
sheet_2['A1'] = str(row[0:1])
sheet_2['B1'] = str(row[1:2])
sheet_2['C1'] = str(row[2:3])
sheet_2['D1'] = str(row[3:4])
sheet_3['A1'] = str(row[0:1])
sheet_3['B1'] = str(row[1:2])
sheet_3['C1'] = str(row[2:3])
sheet_3['D1'] = str(row[3:4])

rows = 2
for header in data['headers']:
    text = header['properties']
    # Обращение по координатам [ряд][колонка]
    sheet_1[rows][0].value = text['Id']
    sheet_1[rows][1].value = text['Name']
    sheet_1[rows][2].value = text['Sid']
    sheet_1[rows][3].value = text['Enabled']
    rows += 1

# Чтобы изменения вступили в силу
# сохраняем книгу
book.save("my_book.xlsx")
book.close()
