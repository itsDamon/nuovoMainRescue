from time import sleep

import numpy as np

from variabiliGlobali import *


def oldDirezione(mat):
    # bianco 1, startBase = Y, startCentro = X
    y = numeroDivisioniMatrice - 1  # inizio matrice dal basso
    x = centroMatrice  # centro iniziale
    # y-1 significa salire, x+1 destra, x-1 sinistra
    while x<6 and y>0:
        if mat[y - 1, x] == 1:  # controllo sopra di uno
            y -= 1  # salgo di uno
            mat[y, x] = 2  # assegno posizione attuale 2
        elif mat[y - 1, x] == 0:
            if mat[y, x - 1] == 1:
                mat[y, x - 1] = 2
                x -= 1
            elif mat[y, x + 1] == 1:
                mat[y, x + 1] = 2
                x += 1

        print(mat)
        print("\n", 'x = ' + str(x), 'y = ' + str(y))
        sleep(1)
        '''if x == centroMatrice:
            return AVANTI, mat
        elif x > centroMatrice:
            return DESTRA, mat
        elif x < centroMatrice:
            return SINISTRA, mat'''


mat = np.zeros((7, 7))

for i in range(6, 2, -1):
    mat[i, 3] = 1
for j in range(3, 7, +1):
    mat[3, j] = 1
print(mat)
a, b = oldDirezione(mat)
print(a, "\n", b)
