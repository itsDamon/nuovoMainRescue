from time import sleep

import cv2
import imutils
from picamera2 import Picamera2

from variabiliGlobali import *

cv2.startWindowThread()  # permette l'aggiornamento di cv2.imshow()
camera = Picamera2()  # assegna la videocamera e assegna il video a camera
camera.configure(
    camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (MAXX, MAXY)}))  # configura la videocamera
camera.controls.Brightness = 0
camera.set_controls({"ExposureTime": EXPOSURE, "AnalogueGain": 1.0, "AeEnable": 0})  # controllo esposizione
camera.start()  # avvia la videocamera
sleep(2)  # pausa 2s


def isNero(immagine, soglia):
    cnts = cv2.findContours(immagine.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        area = w * h
        if soglia < area:
            return 1
    return 0


def filtro(img):  # converte l'immagine in bianco e nero invertito,(nero reale=bianco e viceversa)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte l'immagine da bgr a grayscale
    (T, threshed) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # converte in bianco e nero l'immagine
    threshed = cv2.erode(threshed, None, iterations=3)
    copy = threshed.copy()
    for i in range(numeroDivisioniMatrice):
        for j in range(numeroDivisioniMatrice):
            cv2.rectangle(copy, (MAXX // numeroDivisioniMatrice * j, MAXY // numeroDivisioniMatrice * i),
                          (MAXX // numeroDivisioniMatrice * (j + 1), MAXY // numeroDivisioniMatrice * (i + 1)),
                          (0, 0, 0))
    cv2.imshow("Tresh", copy)  # la mostra a video
    return threshed

def getDirezione(mat):
    # bianco 1, startBase = Y, startCentro = X
    y = numeroDivisioniMatrice - 1  # inizio matrice dal basso
    x = centroMatrice  # centro iniziale
    # y-1 = salire, x+1 = destra, x-1 = sinistra
    while 6 > x >=0 and y>0:
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
        if x == 0 or y == 7 or x == 7 or y == 0:
            break
    #return direzione e matrice
    if x == centroMatrice:
        return AVANTI,mat
    elif x > centroMatrice:
        return DESTRA,mat
    elif x < centroMatrice:
        return SINISTRA,mat
def oldDirezione(mat):
    #bianco 1, startBase = Y, startCentro = X
    startBase = numeroDivisioniMatrice #inizio matrice dal basso
    startCentro = centroMatrice #centro iniziale
    while True:
        if mat[startBase,startCentro] and startBase >= 0:
            startBase +=1
            continue
        elif mat[startBase,startCentro-1] and startCentro >= 0:
            startCentro -=1
            continue
        elif mat[startBase,startCentro] and startCentro <= 6:
            startCentro +=1
            continue
        if startCentro == centroMatrice:
            return AVANTI
        elif startCentro > centroMatrice:
            return DESTRA
        elif startCentro < centroMatrice:
            return SINISTRA



def assegnaDirezione2(mat):
    baseMatrice = numeroDivisioniMatrice-1 #è l'ultima riga della matrice
    centro = mat[baseMatrice,centroMatrice]  # acquisisce il valore della cella centrale
    destra = mat[baseMatrice, centroMatrice + 1]  # acquisisce il valore della cella centrale destra
    sinistra = mat[baseMatrice, centroMatrice - 1]  # acquisisce il valore della cella centrale sinistra
    if centro:
        if mat[baseMatrice-1,centroMatrice]:
            return AVANTI
        else:
            if destra and sinistra:
                return -1
            elif destra:
                return DESTRA
            elif sinistra:
                return SINISTRA
    else:
        if destra and sinistra:
            return -1
        elif destra:
            return DESTRA
        elif sinistra:
            return SINISTRA
        else:
            return 4
