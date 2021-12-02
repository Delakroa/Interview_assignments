import openpyxl
import json

with open('test1.json') as file:
    data = json.load(file)
for header in data['headers']:
    text = header['properties']
    Id = text['Id']
    Name = text['Name']
    Sid = text['Sid']
    Enabled = text['Enabled']
    X = text['X']
    Y = text['Y']
    Width = text['Width']
    Height = text['Height']
    # print(type(text))
    print(Id, Name, Sid, Enabled, X, Y, Width, Height)

# Создаём рабочую книгу
book = openpyxl.Workbook()

# Позиционирование на конкретном листе
# в который мы осуществляем запись
sheet = book.active  # по умолчанию это первый лист

# Обращение к координатам ячейки
sheet['A1'] = 'ID'
sheet['B1'] = 'NAME'
sheet['C1'] = 'SID'
sheet['D1'] = 'ENABLED'
sheet['E1'] = 'X'
sheet['F1'] = 'Y'
sheet['G1'] = 'WIDTH'
sheet['H1'] = 'HEIGHT'

row = 2
for header in data['headers']:
    text = header['properties']
    # Обращение по координатам [ряд][колонка]
    sheet[row][0].value = text['Id']
    sheet[row][1].value = text['Name']
    sheet[row][2].value = text['Sid']
    sheet[row][3].value = text['Enabled']
    sheet[row][4].value = text['X']
    sheet[row][5].value = text['Y']
    sheet[row][6].value = text['Width']
    sheet[row][7].value = text['Height']
    row += 1


# Чтобы изменения вступили в силу
# сохраняем книгу
book.save("my_book.xlsx")
book.close()
