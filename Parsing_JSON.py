import openpyxl
import json

with open('test1.json') as file:
    data = json.load(file)
for header in data['headers']:
    text = header['properties']
    Id = text['Width']
    print(Id)


# print(data['headers'])
# print(data['values'])

# book = openpyxl.Workbook()
#
# sheet = book.active
#
# sheet['A2'] = 100
# sheet['B3'] = 'hello'
#
# book.save("my_book.xlsx")
# book.close()
