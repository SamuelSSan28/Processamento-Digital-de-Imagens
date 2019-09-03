import cv2
import math
import numpy as np


def xy(img):
    return img.shape[0],img.shape[1]

def mostraImagem(img,txt):
    cv2.imshow(txt, img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def negativo(img,L):
    col,lin = xy(img)
    for i in range(col):
        for j in range(lin):
            img[i][j] = L - 1 - img[i][j]

    mostraImagem(img,'Negativo')

def logaritimica(img,c):
    col,lin = xy(img)
    for i in range(col):
        for j in range(lin):
            r  = 1 + img[i][j]/255
            img[i][j] = (c * math.log(r))*255
    mostraImagem(img,'Tranformacao Logaritimica c = ' + str(c))

def gama(img,gamma):
    invGamma =  1/gamma
    col, lin = xy(img)
    for i in range(col):
        for j in range(lin):
            img[i][j] = round(((img[i][j]/255)**gamma)*255)
    mostraImagem(img,"test")


#-----------------MAIN---------------------#
#img1 = cv2.imread('Mamografia.tif',0)
#negativo(img1,255)

#img1 = cv2.imread('Fourrier.tif',0)
#logaritimica(img1,1)

#img1 = cv2.imread('cidade.tif',0)
#gama(img1,4)
