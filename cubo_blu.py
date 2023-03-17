#rom picamera.array import PiRGBArray
from picamera2 import Picamera2, Preview
import cv2
import numpy as np
import imutils
import serial
import time

light_blue = np.array([100,50,50])
dark_blue = np.array([115,255,255])
MAXX=256
MAXY=144
cv2.startWindowThread()   #permette l'aggiornamento di cv2.imshow()
camera = Picamera2()      #assegna la videocamera e assegna il video a camera
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (MAXX, MAXY)})) #configura la videocamera
camera.start()            #avvia la videocamera
time.sleep(2)             #pausa 2s

def vediCubiBlu(mask):
    mask = cv2.inRange(hsv, light_blue, dark_blue)
    cv2.imshow("cubo_blu",mask)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    
    
    if len(cnts) != 0:
        c = max(cnts, key = cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cx = (x+(w//2))     #trova il punto medio
        area=w*h
        print(area)
        
        cy = (y+(h//2))
    
        if area>1000 and area<10400 :
            return (cx, cy)
    return 0

while True:
    im = camera.capture_array()
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    cv2.imshow("Camera", im)
    trovato=vediCubiBlu(im)
    print(trovato)
picam2.close()


