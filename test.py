import numpy as np
from variabiliGlobali import *


def oldDirezione(mat):
    #bianco 1, startBase = Y, startCentro = X
    startBase = numeroDivisioniMatrice-1 #inizio matrice dal basso
    startCentro = centroMatrice #centro iniziale
    while True:
        if mat[startBase,startCentro] and startBase >= 0:
            startBase +=1
            continue
        elif mat[startBase,startCentro-1] and startCentro >= 0 and startCentro <= 6:
            startCentro -=1
            continue
        elif mat[startBase,startCentro] and startCentro <= 6 and startCentro >= 0:
            startCentro +=1
            continue
        if startCentro == centroMatrice:
            return AVANTI
        elif startCentro > centroMatrice:
            return DESTRA
        elif startCentro < centroMatrice:
            return SINISTRA


mat = np.zeros((7, 7))

for i in range(6,2,-1):
    mat[i,3] = 1
for j in range(3,7,+1):
    mat[3,j] = 1
print(mat)
print(oldDirezione(mat))