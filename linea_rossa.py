import time

import cv2
import imutils
import numpy as np
from variabiliGlobali import *

def rosso(im):
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    light_red = np.array([0, 100, 100])
    dark_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv, light_red, dark_red)
    mask = mask [MINY2:MAXY , MAXX//3 : MAXX//3*2]
    cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cx = (x + (w // 2))  # trova il punto medio
        area = w * h
        if areaValidaMin < area:
            return True
    return False

