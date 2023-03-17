from time import sleep

import cv2
from picamera2 import Picamera2
import numpy as np


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
    b = 0   #blacnk numero pixel neri
    w = 0    #white numero pixel bianchi
    for iy in range(0, immagine.shape[0], 1):
        for ix in range(0, immagine.shape[1], 1):
            if immagine[iy, ix] == 255:
                b += 1
            else:
                w += 1
    p2 = 100*b//(b+w)
    if p2 > soglia:
        return 1
    else:
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
