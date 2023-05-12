from time import sleep

import numpy as np

from variabiliGlobali import *


def oldDirezione(mat):
    checkX = 'init'
    checkY = 'init'
    # bianco 1, startBase = Y, startCentro = X
    y = numeroDivisioniMatrice - 1  # inizio matrice dal basso
    x = centroMatrice  # centro iniziale
    # y-1 significa salire, x+1 destra, x-1 sinistra
    while 6 > x >=0 and y>0:
        #if(x == checkX and y == checkY): #break se si ripete
         #   print('\nRipetuto.')
          #  break
        mat[y,x]= 0 #posizione iniziale a 0
        if mat[y - 1, x]:  # controllo sopra di uno
            y -= 1  # scorro sopra di uno
        elif mat[y - 1, x] == 0: # se sopra 0
            if mat[y, x - 1]: #controllo a sinistra
                x -= 1 # scorro sinistra di uno
                break
            elif mat[y, x + 1]: #controllo a sinistra
                x += 1 #scorro destra di uno
                break
            break
        checkX = x
        checkY = y
        print('\n',mat)
        print('x =',x,',', 'y =',y)
        #sleep(1)
        if x == 0 or y == 7 or x == 7 or y == 0:
            break

    if x == centroMatrice:
        return AVANTI,mat
    elif x > centroMatrice:
        return DESTRA,mat
    elif x < centroMatrice:
        return SINISTRA,mat

#test purpose
#genera linea di 1 nella matrice
scelta = "Prova"
while(scelta != -1):
    mat = np.zeros((7, 7))
    scelta = int(input("Test(4 exit / Return values Avanti 3 Destra 2 Sinistra 1): \n1.Linea dritta \n2.Curva Destra \n3.Curva Sinistra \n4.Forma + \n"
                       "5.Linea dritta interrotta \n6.Diagonale Sinistra \n7.Diagonale Destra \n-> "))
    if(scelta == 1):
        for i in range(6):
            mat[i, 3] = 1
    elif(scelta ==2):
        for i in range(6, 2, -1):
            mat[i, 3] = 1
        for j in range(3, 7, +1):
            mat[3, j] = 1
    elif(scelta ==3):
        for i in range(6, 2, -1):
            mat[i, 3] = 1
        for j in range(0, 4, +1):
            mat[3, j] = 1
    elif (scelta == 4):
        for i in range(7):
            mat[i, 3] = 1
        for j in range(7):
            mat[3, j] = 1
    elif (scelta == 5):
        for i in range(2,7):
            mat[i, 3] = 1
    elif (scelta == 6):
        for i in range(4,7):
            mat[i, 3] = 1
        mat[5, 3] = 1
        mat[3, 2] = 1
        mat[4, 2] = 1
        mat[3, 1] = 1
        mat[2, 1] = 1
        mat[2, 0] = 1
    elif (scelta == 7):
        for i in range(4,7):
            mat[i, 3] = 1
        mat[5, 3] = 1
        mat[3, 4] = 1
        mat[4, 4] = 1
        mat[3, 5] = 1
        mat[2, 5] = 1
        mat[2, 6] = 1
    if(scelta != -1):
        #controllo matrice generato con gli 1
        print('Start\n',mat,'\n')
        a, b = oldDirezione(mat)
        #print risultato
        print(b,'\n','return: ',a)
print("Exit")
