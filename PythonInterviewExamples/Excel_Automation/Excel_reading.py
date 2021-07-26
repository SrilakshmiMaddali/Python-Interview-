import openpyxl
import os



workbook = openpyxl.load_workbook('Submission Details-3.xlsx')
sheet = workbook['Sheet1']
cell=sheet['D5']
print(cell.value)

for i in range(1,10):
    print(i, sheet.cell(row=i,column=4).value)