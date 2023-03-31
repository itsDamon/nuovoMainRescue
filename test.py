from time import sleep

import numpy as np

from variabiliGlobali import *


def oldDirezione(mat):
    # bianco 1, startBase = Y, startCentro = X
    y = numeroDivisioniMatrice - 1  # inizio matrice dal basso
    x = centroMatrice  # centro iniziale
    # y-1 significa salire, x+1 destra, x-1 sinistra

    while 6 > x >=0 and y>0:
        mat[y,x]= 0 #posizione iniziale a 0
        if mat[y - 1, x]:  # controllo sopra di uno
            y -= 1  # scorro sopra di uno
        elif mat[y - 1, x] == 0: # se sopra 0
            if mat[y, x - 1]: #controllo a sinistra
                x -= 1 # scorro sinistra di uno
            elif mat[y, x + 1]: #controllo a sinistra
                x += 1 #scorro destra di uno
        mat[y, x] = 2 # assegno posizione attuale 2
        print(mat)
        print("\n", 'x = ' + str(x), 'y = ' + str(y))
        sleep(1)
        if x == 0 or y == 7 or x ==7 or y == 0:
            break

    print("================================")
    if x == centroMatrice:
        return AVANTI, mat
    elif x > centroMatrice:
        return DESTRA, mat
    elif x < centroMatrice:
        return SINISTRA, mat

#test purpose
#genera linea di 1 nella matrice
mat = np.zeros((7, 7))
for i in range(6, 2, -1):
    mat[i, 3] = 1
#for j in range(3, 7, +1):
for j in range(0, 4, +1):
    mat[3, j] = 1

#controllo matrice generato con gli 1
print('\n',mat)
a = oldDirezione(mat)
#print risultato
print('\n','return value:', a)
