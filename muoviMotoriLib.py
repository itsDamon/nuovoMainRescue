n = 10


def avanti(ser):
    for _ in range(n):
        ser.write(b'a')


def stop(ser):
    for _ in range(n):
        ser.write(b'w')


def destra(ser):
    for _ in range(n):
        ser.write(b'd')


def Sdestra(ser):
    for _ in range(n):
        ser.write(b'D')


def sinistra(ser):
    for _ in range(n):
        ser.write(b's')


def Ssinistra(ser):
    for _ in range(n):
        ser.write(b'S')


def retro(ser):
    for _ in range(n):
        ser.write(b'b')


def destra90(ser):
    for _ in range(n):
        ser.write(b'r')


def sinistra90(ser):
    for _ in range(n):
        ser.write(b'l')


def curva180(ser):
    for _ in range(n):
        ser.write(b'T')
