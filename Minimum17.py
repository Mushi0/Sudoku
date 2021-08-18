import requests
import re

URL = 'https://www.free-sudoku.com/sudoku.php?dchoix=evil'
FILE = 'Sudoku17.dat'

with open(FILE, 'w') as f:
    f.write('n: 3')
    for i in range(1, 101):
        f.write(']\n\nSudoku_' + str(i) + ': [')
        
        response = requests.get(URL)
        print('Open the website. i = ' + str(i))
        html = response.text

        for j in range(1, 82):
            str1 = '<div\sid="' + str(j)
            result1 = re.findall(str1 + '"\sclass=(.*?)\s', html)[0]
            # print(result1)
            
            if(result1 == '"pred2"'):
                print('j = ' + str(j))
                result2 = re.findall(str1 + '".*?\s>(\d)</div>', html)[0]
                print(result2)
                r = (j - 1)//9 + 1
                c = j%9
                if(c == 0):
                    c = 9
                f.write('\n(' + str(r) + ' ' + str(c) + ') ' + str(result2))
