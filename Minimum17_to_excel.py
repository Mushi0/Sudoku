import xlwt
import re

FILE_READ = 'Sudoku17.dat'
FILE_WRITE = 'Sudoku.xls'

workbook = xlwt.Workbook(encoding = 'utf-8')
worksheet = workbook.add_sheet('Sudoku_17')

i = -2
r = -10
with open(FILE_READ, 'r') as f:
    for line in f:
        if(line.startswith('Sudoku_')):
            print('Sudoku')
            i = 0
            r += 10
        if(i >= 1 and i <= 17):
            result = re.findall('\((\d)\s(\d)\)\s(\d)', line)[0]
            print(result[2])
            worksheet.write(int(result[0]) + r, int(result[1]), int(result[2]))
        i += 1

workbook.save(FILE_WRITE)
