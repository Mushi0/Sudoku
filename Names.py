S = []
FILE = 'Sudoku_3_8.dat'

with open(FILE, 'r') as f:
    for line in f:
        if(line.startswith('sudoku')):
            S.append(line.split(':')[0])

print(S)

with open(FILE, 'a') as f:
    f.write('names: [')
    for s in S:
        f.write('"' + s + '" ')
    f.write(']')
