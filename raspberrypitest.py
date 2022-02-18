from picamera import PiCamera
from time import sleep
import cv2
import numpy as np
import os


lokasjon = "SKRIV INN PATH HER MED / TIL SLUTT"

bildenavn1, bildenavn2 = "bilde1", "bilde2"
bildebane1, bildebane2 = lokasjon + bildenavn1 + ".jpg", lokasjon + bildenavn2 + ".jpg"


def bevegelse(bilde1, bilde2):
    #lagrer informasjon om bildene
    bilde1_lest = cv2.imread(bildebane1)
    bilde2_lest = cv2.imread(bildebane2)

    #sjekker om disse bildene er like ved å bruke informasjonen hentet over
    if bilde1_lest.shape == bilde2_lest.shape:
        return True
    else:
        return False


def main():
    #for å gjøre klart kamera
    kamera = PiCamera()

    #loop for å sjekke bevegelse
    while True:

        #for å forhindre at bilder blir lagret med samme navn og blir overskrevet
        indeks = 1

        bilde1 = kamera.capture(bildebane1)
        sleep(2)
        bilde2 = kamera.capture(bildebane2)

        if bevegelse(bilde1, bilde2):
            kamera.capture(lokasjon + "bevegelsesbilde" + str(indeks) ".jpg")
            #for å forhindre at bilder blir overskrevet
            indeks += 1

        os.remove(bildebane1)
        os.remove(bildebane2)

        sleep(0.5)


if __name__ == "__main__":
    main()