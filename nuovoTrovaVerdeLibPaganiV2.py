import cv2
import imutils
import numpy as np

# soglia nero
# controllo alto e tolto <30 dal ciclo
# allargato area sopra check
# abbassato soglia quanto nero per essere true
# importante ferma i motori quando è valido il verde

light_green = np.array([36, 50, 50])
dark_green = np.array([85, 255, 255])

#non rimuovere

'''def isverde(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, light_green, dark_green)
    cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cv2.imshow("isVerde", mask)
    if len(cnts) != 0:
        c = max(cnts, key=cv2.contourArea)
        x, y, w, h = cv2.boundingRect(c)
        cx = (x + (w // 2))  # trova il punto medio
        area = w * h
        if area > 200:
            return True
    return False'''


def trovaVerde(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, light_green, dark_green)
    mask = cv2.erode(mask, None, iterations=3)
    cv2.imshow("green", mask)  # debug
    cnts = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    direzione = -1
    if len(cnts) > 0:
        listaAree = []
        attivati = False
        for c in cnts:
            x, y, w, h = cv2.boundingRect(c)
            if (w * h) < 500:  # da settare con quello reale
                continue
            listaAree.append(nero(img, x, y, w, h))
            # se non arriva un verde vicino non inizio a valutare se curvare
            if y > 100:
                attivati = True
        if attivati == False:  # non fare nulla
            return -1
        ###############qui spengo i motori e guardo meglio
        ###############tipo return -2, se ritorna -2 rifaccio il check ma da fermo
        # creo una lista solo di ciò che è valido
        valide = []
        for area in listaAree:
            # se l'area verde è valida
            if area["sopra"] == True:
                valide.append(area)

        print("valide:", valide)
        quanti = len(valide)
        if quanti == 2:
            direzione = 0  # inversione (controllato nel main)
        elif quanti == 1:
            curvo = valide[0]
            if curvo["sinistra"] == True or curvo["destra"] == False:
                direzione = 1  # destra (controllato nel main)
            else:
                direzione = 2  # sinistra (controllato nel main)

        print("direzione ", direzione)
        return direzione


def isNero(immagine, soglia):
    b = 0
    w = 0
    for iy in range(0, immagine.shape[0], 1):
        for ix in range(0, immagine.shape[1], 1):
            if immagine[iy, ix] == 255:
                w += 1
            else:
                b += 1
    if w == 0:
        print("noimg")
        return False
    p2 = w / (w + b) * 100
    if p2 > soglia:
        return True
    else:
        return False


def nero(img, x, y, w, h):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converte l'immagine da bgr a grayscale
    (T, threshed) = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)  # converte in bianco e nero l'immagine
    threshed = cv2.erode(threshed, None, iterations=3)
    copy = threshed.copy()
    print("x = " + str(x) + " y = " + str(y) + " w = " + str(w) + " h = " + str(h))
    cv2.rectangle(copy, (x, y), (x + w, y + h), (255, 0, 0))
    cv2.imshow("nero", copy)  # la mostra a video
    cx = x + (w // 2)
    cy = y + (h // 2)

    sopra = copy[y - 20:y - 5, cx - 20:cx + 20]
    cv2.rectangle(img, (cx - 20, y - 20), (cx + 20, y - 5), (0, 0, 255))

    sotto = copy[y + h + 5:y + h + 20, cx - 10:cx + 10]
    cv2.rectangle(img, (cx - 10, y + h + 5), (cx + 10, y + h + 20), (0, 0, 255))

    destra = copy[cy - 10:cy + 10, x + w + 5:x + w + 20]
    cv2.rectangle(img, (x + w + 5, cy - 10), (x + w + 20, cy + 10), (0, 0, 255))

    sinistra = copy[cy - 10:cy + 10, x - 20: x - 1]
    cv2.rectangle(img, (x - 20, cy - 10), (x - 1, cy + 10), (0, 0, 255))

    cv2.imshow("sotto", img)
    area = {
        "sopra": isNero(sopra, 10),
        "sotto": isNero(sotto, 10),
        "destra": isNero(destra, 10),
        "sinistra": isNero(sinistra, 10)
    }
    if x < 20:
        area["sinistra"] = False
    if y < 30:
        area["sopra"] = False
    if (y + h) > 450:
        area["basso"] = False
    if x + w > 620:
        area["destra"] = False

    return area

'''cap = cv2.VideoCapture(0)
if not cap.isOpened():
    cap.open(0)

while True:
    ret, image = cap.read(0)
    cv2.waitKey(1)
    cv2.imshow('window', image)
    trovaVerde(image)'''