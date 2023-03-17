from picamera2 import Picamera2, Preview
import cv2
import numpy as np
import imutils
from time import sleep
from trovaVerdeLib import isverde

MAXX=256
MAXY=144
cv2.startWindowThread()   #permette l'aggiornamento di cv2.imshow()
camera = Picamera2()      #assegna la videocamera e assegna il video a camera
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (MAXX, MAXY)})) #configura la videocamera
camera.controls.Brightness = 0
camera.set_controls({"ExposureTime": 30000, "AnalogueGain": 1.0}) # controllo esposizione
camera.start()            #avvia la videocamer
sleep(2)          

def filtro(img):        #converte l'immagine in bianco e nero invertito,(nero reale=bianco e viceversa)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#converte l'immagine da bgr a grayscale
    (T, threshed) = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)#converte in bianco e nero l'immagine
    threshed=cv2.erode(threshed,None,iterations=3)
    cv2.imshow("Tresh", threshed)#la mostra a video
    return threshed

while True:
    im = camera.capture_array()    
    #im = cv2.flip(im, 0) #decommentare in caso che la videocamera è al contrario
    cv2.imshow("Camera", im)
    mask = filtro(im)
    isverde(im)

camera.close()
