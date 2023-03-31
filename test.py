import numpy as np
from variabiliGlobali import *


def oldDirezione(mat):
    #bianco 1, startBase = Y, startCentro = X
    startBase = numeroDivisioniMatrice-1 #inizio matrice dal basso
    startCentro = centroMatrice #centro iniziale
    while True:
        if startBase > -1 and startCentro > 0 and startCentro < 6:
            if mat[startBase+1,startCentro]:
                mat[startBase+1,startCentro] = 0
                startBase +=1
            else:
                if mat[startBase,startCentro-1] :
                    mat[startBase - 1, startCentro - 1] = 0
                    startCentro -=1
                elif mat[startBase,startCentro+1]:
                    mat[startBase - 1, startCentro] = 0
                    startCentro += 1
        if startCentro == centroMatrice:
            return AVANTI,mat
        elif startCentro > centroMatrice:
            return DESTRA,mat
        elif startCentro < centroMatrice:
            return SINISTRA,mat


mat = np.zeros((7, 7))

for i in range(6,2,-1):
    mat[i,3] = 1
for j in range(3,7,+1):
    mat[3,j] = 1
print(mat)
a, b  = oldDirezione(mat)
print(a,"\n", b)