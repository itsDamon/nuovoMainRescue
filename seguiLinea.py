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
        if soglia < area < 10000:
            return 1
        else:
            n = 0
            n += sogliaRitorno(immagine[y: y + 5, x: x + 5], 30)
            n += sogliaRitorno(immagine[y:y + 5, w - 5:w], 30)
            n += sogliaRitorno(immagine[h - 5:h, x:x + 5], 30)
            n += sogliaRitorno(immagine[h - 5:h, w - 5:w], 30)
            print(n)
            if n > 0:
                return 0
    return 1


def sogliaRitorno(immagine, soglia):
    b = 0
    w = 0
    for iy in range(0, immagine.shape[0], 1):
        for ix in range(0, immagine.shape[1], 1):
            if immagine[iy, ix] == 255:
                w += 1
            else:
                b += 1
    try:
        p2 = w / (w + b) * 100
    except:
        print("pino")
        return 0
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
