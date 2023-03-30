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

def oldDirezione(mat):
    pos = centroMatrice
    for _ in range(numeroDivisioniMatrice):
        if centro ==1:
            print ("")

def assegnaDirezione(mat):
    if mat[numeroDivisioniMatriceMatrice,centroMatrice] == 1: #guarda se il centro basso della matrice è pieno
        destra = mat[numeroDivisioniMatrice,centroMatrice+1] # vede se a destra vale 1
        sinistra = mat[numeroDivisioniMatrice,centroMatrice-1] #vede se a sinistra vale 1
        if destra == sinistra == 1: # destra e sinistra pieni vai dritto aka gestione incrocio
            return 3
        elif destra == 1: # correggi a destra perchè vede linea
            return 2
        elif sinistra == 1: #correggi a sinistra perchè vede linea
            return 1
        else:               #nel dubbio dritto
            return 3

def assegnaDirezione(mat):
    centro = [numeroDivisioniMatriceMatrice,centroMatrice] # acquisisce il valore della cella centrale
    destra = mat[numeroDivisioniMatrice, centroMatrice + 1] # acquisisce il valore della cella centrale destra
    sinistra = mat[numeroDivisioniMatrice, centroMatrice - 1]  # acquisisce il valore della cella centrale sinistra
