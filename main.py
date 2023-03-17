import RPi.GPIO as GPIO
import serial

from linea_rossa import *
from muoviMotoriLib import *
from seguiLinea import *

# motori, sensori = motoriOSensori()
# motori = serial.Serial("/dev/ttyACM0", 9600)

# set pin
pinReset = 23  # pin 16
# set pin mode
GPIO.setmode(GPIO.BCM)  # enable gpio
GPIO.setup(pinReset, GPIO.IN)  # set pin output
# setup thread per reset
GPIO.setup(pinReset, GPIO.IN, pull_up_down=GPIO.PUD_UP)
# variabili
global STATO, direzione
STATO = 1
direzione = 3


def reset():
    global STATO, direzione
    stop(motori)
    direzione = 3
    if STATO == 0:
        STATO = 1
    else:
        STATO = 0
    sleep(2)


def setOstacolo():
    global STATO
    stop(motori)
    STATO = 2


# GPIO.add_event_detect(pinReset, GPIO.FALLING, callback=reset, bouncetime=2000)
# GPIO.add_event_detect(pinOstacolo, GPIO.RISING, callback=setOstacolo, bouncetime=1000)

if __name__ == '__main__':
    while True:
        if GPIO.input(pinReset) == 0:
            print("reset")
            reset()
        if STATO == 0:
            print("Stato 0")
            stop(motori)
        elif STATO == 1:
            # Prende immagini dalla cam e le mostra a ogni iterazione del ciclo
            im = camera.capture_array()
            # if rosso(im):
            #     STATO = 0
            #     print("ROSSO")
            #     continue
            # im = cv2.flip(im, 0) #decommentare in caso che la videocamera è al contrario
            copia = im.copy()
            for i in range(7):
                for j in range(7):
                    cv2.rectangle(copia, (MAXX // 7 * j, MAXY // 7 * i), (MAXX // 7 * (j + 1), MAXY // (i + 1)))

            cv2.imshow("Camera", copia)  # mostra l'immagine a video

            '''
            verde = trovaVerde(im)
            print(verde)
            if verde == 0:
                avanti(motori)
                sleep(0.82)
                curva180(motori)
                sleep(3)
                print("vstop")
            if verde == 1:  # gira a destra
                avanti(motori)
                sleep(0.82)
                destra90(motori)
                sleep(3)
                print("Vdestra")
            elif verde == 2:  # gira a sinistra
                avanti(motori)
                sleep(0.82)
                sinistra90(motori)
                sleep(3)
                print("Vsinistra")
            '''

            mask = filtro(im)  # chiama la funzione filtro e assegna il valore a mask



        elif STATO == 2:
            print("ostacolo")
            # ostacolo(motori)
            STATO = 1
