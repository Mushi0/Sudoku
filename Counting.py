import numpy as np

n = 4
N = 7
NN = 15

for i in range(N, NN + 1):
    FILE = 'Sudoku_' + str(n) + '_' + str(i) + '.dat'

    print(FILE)

    L = []
    l = 0

    with open(FILE, 'r') as f:
        for line in f:
            if(line.startswith('sudoku')):
                l = 0
            l += 1
            if(line.startswith(']')):
                L.append(l - 1)

    print(L)
    print(np.mean(L))
